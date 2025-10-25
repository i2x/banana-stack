import { useEffect, useState } from "react";
import { getDiseases } from "../services/api";
import DiseaseCard from "../components/ArticlesPage/DiseaseCard";

interface Disease {
  disease_id: number;
  name: string;
  description: string;
  symptoms?: string;
  image_example?: string | null;
}

interface DiseaseResponse {
  count: number;
  total_pages: number;
  current_page: number;
  page_size: number;
  results: Disease[];
}

export default function Articles() {
  const [data, setData] = useState<DiseaseResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [page, setPage] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const res = await getDiseases(page, 3); // ส่ง page, size
        setData(res);
      } catch (err: any) {
        console.error(err);
        setError("ไม่สามารถโหลดข้อมูลโรคได้");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [page]);

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h2 className="text-3xl font-bold mb-6">📚 Banana Diseases Articles</h2>

      {loading && <p className="text-gray-600">กำลังโหลดข้อมูล...</p>}
      {error && (
        <div className="p-3 rounded-xl bg-red-50 text-red-700 border border-red-200">
          {error}
        </div>
      )}

      <div className="grid gap-6">
        {data?.results && data.results.length > 0 ? (
          data.results.map((disease) => (
            <DiseaseCard key={disease.disease_id} disease={disease} />
          ))
        ) : (
          !loading && <p className="text-gray-500">ไม่มีข้อมูลโรค</p>
        )}
      </div>

      {/* Pagination controls */}
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
