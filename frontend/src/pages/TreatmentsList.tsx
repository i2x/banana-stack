import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { getTreatments } from "../services/api";
import TreatmentCard from "../components/TreatmentListPage/TreatmentCard";

interface Treatment {
  treatment_id: number;
  method?: string;
  source?: string;
  disease: number;
}

interface TreatmentResponse {
  count: number;
  total_pages: number;
  current_page: number;
  page_size: number;
  results: Treatment[];
}

export default function TreatmentsList() {
  const { diseaseId } = useParams<{ diseaseId: string }>();
  const [data, setData] = useState<TreatmentResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [page, setPage] = useState(1);

  useEffect(() => {
    if (!diseaseId) return;
    const fetchData = async () => {
      try {
        setLoading(true);
        const res = await getTreatments(Number(diseaseId), page, 5);
        setData(res);
      } catch (err: any) {
        console.error(err);
        setError("ไม่สามารถโหลดข้อมูลการรักษาได้");
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [diseaseId, page]);

  return (
    <div className="max-w-3xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-4">💊 วิธีการรักษา</h2>

      {loading && <p className="text-gray-600">กำลังโหลด...</p>}
      {error && (
        <div className="p-3 rounded-xl bg-red-50 text-red-700 border border-red-200">
          {error}
        </div>
      )}

      {/* รายการ treatments */}
      {data?.results?.length ? (
        <div className="space-y-4">
          {data.results.map((t) => (
            <TreatmentCard
              key={t.treatment_id}
              method={t.method}
              source={t.source}
            />
          ))}
        </div>
      ) : (
        !loading && <p className="text-gray-500">ไม่มีข้อมูลการรักษา</p>
      )}

      {/* Pagination */}
      {data && data.total_pages > 1 && (
        <div className="flex justify-center items-center gap-4 mt-6">
          <button
            onClick={() => setPage((p) => Math.max(p - 1, 1))}
            disabled={page === 1}
            className="px-3 py-2 rounded bg-gray-200 disabled:opacity-50"
          >
            ◀ ก่อนหน้า
          </button>
          <span>
            หน้า {data.current_page} / {data.total_pages}
          </span>
          <button
            onClick={() => setPage((p) => Math.min(p + 1, data.total_pages))}
            disabled={page === data.total_pages}
            className="px-3 py-2 rounded bg-gray-200 disabled:opacity-50"
          >
            ถัดไป ▶
          </button>
        </div>
      )}
    </div>
  );
}
