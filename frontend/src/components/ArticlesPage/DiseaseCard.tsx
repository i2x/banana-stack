import { useNavigate } from "react-router-dom";

interface Disease {
  disease_id: number;
  name: string;
  description: string;
  symptoms?: string;
  image_example?: string | null;
}


export default function DiseaseCard({ disease }: { disease: Disease }) {
  const navigate = useNavigate();

  const imageSrc = disease.image_example
    ?  disease.image_example
    : "/images/no-image-available.jpg";

  return (
    <div
      onClick={() => navigate(`/treatments/list/${disease.disease_id}`)}
      className="p-5 border rounded-xl shadow bg-white hover:shadow-md transition cursor-pointer"
    >
      {/* ชื่อโรค */}
      <h3 className="text-xl font-semibold text-green-700 mb-2">
        {disease.name}
      </h3>

      {/* รูปภาพ */}
      <img
        src={imageSrc}
        alt={disease.name}
        className="w-full h-48 object-cover rounded-lg mb-3"
      />

      {/* รายละเอียด */}
      <p className="text-gray-700 mb-2">
        {disease.description || "ไม่มีคำอธิบาย"}
      </p>

      {/* อาการ */}
      {disease.symptoms && (
        <p className="text-sm text-gray-600">
          <span className="font-medium">อาการ: </span>
          {disease.symptoms}
        </p>
      )}
    </div>
  );
}
