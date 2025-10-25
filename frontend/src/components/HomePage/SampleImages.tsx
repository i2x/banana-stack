import { useState } from "react";

export default function SampleImages() {
  const [open, setOpen] = useState(false);

  const samples = [
    { src: "/images/BlackSigatokaDisease.jpg", label: "Banana Black Sigatoka" },
    { src: "/images/HealthyLeaf.jpg", label: "Banana Healthy Leaf" },
  ];

  return (
    <div className="mt-10 pb-10">
      {/* ปุ่ม toggle */}
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center justify-between w-full px-4 py-3 rounded-xl bg-green-600 text-white font-semibold shadow hover:bg-green-700 transition"
      >
        🖼️ ตัวอย่างการถ่ายภาพใบตอง
        <span className="ml-2">{open ? "▲" : "▼"}</span>
      </button>

      {/* รูปภาพจาก public */}
      {open && (
        <div className="mt-4 flex justify-center gap-6 flex-wrap">
          {samples.map((s, idx) => (
            <div
              key={idx}
              className="rounded-xl overflow-hidden shadow-md border bg-white"
            >
              <img
                src={s.src}
                alt={s.label}
                className="w-64 h-48 object-cover"
              />
              <div className="p-3 text-center text-sm font-medium text-gray-700">
                {s.label}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
