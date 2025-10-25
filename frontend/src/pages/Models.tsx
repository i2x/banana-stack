import React, { useEffect, useState } from "react";
import { getModels } from "../services/api";
import ModelUsage from "../components/ModelsPage/ModelUsage";

interface Model {
  model_id: number;
  file_name: string;
  file_path: string;
  version: string;
  uploaded_at: string;
}

interface ModelsResponse {
  count: number;
  total_pages: number;
  current_page: number;
  results: Model[];
}

const Models: React.FC = () => {
  const [models, setModels] = useState<Model[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    const fetchModels = async () => {
      try {
        setLoading(true);
        const data: ModelsResponse = await getModels(page, 5);
        setModels(data.results);
        setTotalPages(data.total_pages);
      } catch (err) {
        console.error(err);
        setError("โหลดข้อมูลโมเดลไม่สำเร็จ");
      } finally {
        setLoading(false);
      }
    };

    fetchModels();
  }, [page]);

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6">Models</h2>

      {loading && <p>กำลังโหลด...</p>}
      {error && <p className="text-red-600">{error}</p>}

      {!loading && !error && models.length === 0 && <p>ไม่มีโมเดล</p>}

      <div className="grid gap-4">
        {models.map((m) => (
          <div key={m.model_id} className="mb-6 p-4 border rounded-lg bg-white shadow">
            <h3 className="text-xl font-semibold">{m.file_name}</h3>
            <p>📦 Version: {m.version}</p>
            <p>📅 Uploaded: {new Date(m.uploaded_at).toLocaleString()}</p>
            <a
              href={m.file_path}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-2 inline-block px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
            >
              ดาวน์โหลดโมเดล
            </a>

            <ModelUsage fileName={m.file_name} />
          </div>
        ))}
      </div>

      {/* 🔥 Pagination */}
      <div className="flex items-center gap-3 mt-6">
        <button
          onClick={() => setPage((p) => Math.max(p - 1, 1))}
          disabled={page === 1}
          className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
        >
          Prev
        </button>
        <span className="text-gray-700">
          Page {page} / {totalPages}
        </span>
        <button
          onClick={() => setPage((p) => Math.min(p + 1, totalPages))}
          disabled={page === totalPages}
          className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default Models;
