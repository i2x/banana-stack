import { useState } from "react";

export default function HowToUse() {
  const [open, setOpen] = useState(false);

  const steps = [
    {
      title: "เลือกหรืออัปโหลดภาพใบตอง",
      description:
        "สามารถเลือกไฟล์จากเครื่อง หรือหากใช้คอมพิวเตอร์สามารถลากรูปใบตองมาวางได้เลย",
    },
    {
      title: "กดปุ่ม 'ทำนายโรค'",
      description: "ระบบจะส่งภาพไปให้โมเดล CNN ประมวลผลและตรวจสอบอาการ",
    },
    {
      title: "รอผลการวิเคราะห์",
      description:
        "ระบบจะแสดงชื่อโรค ความมั่นใจ (%) และคำแนะนำเบื้องต้น",
    },
    {
      title: "ดูรายละเอียด",
      description:
        "สามารถนำผลการวิเคราะห์ไปใช้ประกอบการตัดสินใจ หรือปรึกษาผู้เชี่ยวชาญเพิ่มเติม",
    },
  ];

  return (
    <div className="mt-10 ">
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center justify-between w-full px-4 py-3 rounded-xl bg-green-600 text-white font-semibold shadow hover:bg-green-700 transition"
      >
        📖 วิธีใช้งาน
        <span className="ml-2">{open ? "▲" : "▼"}</span>
      </button>

      {open && (
        <div className="mt-4 space-y-4">
          {steps.map((step, idx) => (
            <div
              key={idx}
              className="flex items-start gap-3 p-4 rounded-xl border bg-gray-50 shadow-sm"
            >
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-green-600 text-white flex items-center justify-center font-bold">
                {idx + 1}
              </div>
              <div>
                <p className="font-medium text-gray-800">{step.title}</p>
                <p className="text-sm text-gray-600">{step.description}</p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
