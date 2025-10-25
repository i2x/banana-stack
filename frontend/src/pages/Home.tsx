import { useState, useRef } from "react";
import { predictImage } from "../services/api";
import HowToUse from "../components/HomePage/HowToUse";
import SampleImages from "../components/HomePage/SampleImages";
import { Link } from "react-router-dom";

interface Disease {
  disease_id: number;
  name: string;
  description: string;
}

interface PredictionResult {
  prediction_id: number;
  disease: Disease;
  confidence: number;
  predicted_at: string;
  image_url: string | null;
}

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState("");
  const [result, setResult] = useState<PredictionResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const inputRef = useRef<HTMLInputElement | null>(null);

  const onPickFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const f = e.target.files?.[0];
    if (!f) return;
    setFile(f);
    setResult(null);
    setError("");
    const url = URL.createObjectURL(f);
    setPreview(url);
  };

  const onDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    const f = e.dataTransfer.files?.[0];
    if (!f) return;
    if (!f.type.startsWith("image/")) {
      setError("กรุณาเลือกไฟล์รูปภาพเท่านั้น");
      return;
    }
    setFile(f);
    setResult(null);
    setError("");
    const url = URL.createObjectURL(f);
    setPreview(url);
  };

  const onDragOver = (e: React.DragEvent<HTMLDivElement>) => e.preventDefault();

  const reset = () => {
    setFile(null);
    setPreview("");
    setResult(null);
    setError("");
    if (inputRef.current) inputRef.current.value = "";
  };

  const submit = async (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    if (!file) return setError("กรุณาอัปโหลดรูปใบตองก่อน");
    try {
      setLoading(true);
      setError("");
      const res = await predictImage(file);
      setResult(res.data);
    } catch (err: any) {
      console.error(err);
      const msg =
        err?.response?.data?.message ||
        err.message ||
        "เกิดข้อผิดพลาดในการทำนาย";
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-6">
      <h2 className="text-3xl font-bold text-black mb-4">
        ทำนายโรคจากใบตอง 🍌
      </h2>

      <div className="mt-6 space-y-6">
        <HowToUse />
        <SampleImages />
      </div>


      {/* Drop Zone / Upload */}
      <div
        onDrop={onDrop}
        onDragOver={onDragOver}
        className="border-2 border-dashed rounded-2xl p-6 flex flex-col items-center justify-center gap-4 bg-white shadow-sm"
      >
        {preview ? (
          <img
            src={preview}
            alt="preview"
            className="w-full max-w-full max-h-80 h-auto rounded-xl object-contain"
          />
        ) : (
          <div className="text-center text-gray-600">
            <p className="font-medium">ลากรูปใบตองมาวางที่นี่</p>
            <p className="text-sm">หรือเลือกไฟล์จากเครื่อง</p>
          </div>
        )}

        <div className="flex flex-wrap items-center gap-3">
          <input
            ref={inputRef}
            type="file"
            accept="image/*"
            onChange={onPickFile}
            className="block text-sm"
          />
          <button
            onClick={submit}
            disabled={loading || !file}
            className="px-4 py-2 rounded-xl shadow bg-green-600 text-white hover:bg-green-700 disabled:opacity-50"
          >
            {loading ? "กำลังทำนาย..." : "ทำนายโรค"}
          </button>
          {file && (
            <button
              type="button"
              onClick={reset}
              className="px-3 py-2 rounded-xl border shadow-sm"
            >
              ล้างค่า
            </button>
          )}
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="mt-4 p-3 rounded-xl bg-red-50 text-red-700 border border-red-200">
          {error}
        </div>
      )}

      {/* Prediction Result */}
      {result && (
        <div className="mt-6">
          <h3 className="text-xl font-semibold mb-4">ผลการทำนาย</h3>

          <div className="rounded-2xl border p-6 bg-white shadow-md space-y-3">
            <p className="text-sm text-gray-500">โรคที่พบ</p>
            <p className="text-2xl font-bold text-red-600">
              {result.disease?.name}
            </p>

            {typeof result.confidence !== "undefined" && (
              <p className="text-gray-700">
                ความมั่นใจ:{" "}
                <span className="font-medium">
                  {(Number(result.confidence) * 100).toFixed(1)}%
                </span>
              </p>
            )}

            {result.disease?.description && (
              <p className="text-gray-600">
                <span className="font-medium">รายละเอียด: </span>
                {result.disease.description}
              </p>
            )}

            <p className="text-xs text-gray-400">
              วิเคราะห์เมื่อ:{" "}
              {new Date(result.predicted_at).toLocaleString("th-TH")}
            </p>

            {/* ✅ ปุ่มอ่านข้อมูลเพิ่มเติม */}
            <Link
              to={`/treatments/list/${result.disease?.disease_id}`}
              className="inline-block mt-4 px-4 py-2 rounded-xl bg-blue-600 text-white hover:bg-blue-700"
            >
              อ่านข้อมูลการรักษาเพิ่มเติม
            </Link>
          </div>
        </div>
      )}

    </div>
  );
}
