export default function About() {
  const diseases = [
    "Banana Yellow Sigatoka Disease",
    "Banana Panama Disease",
    "Banana Moko Disease",
    "Banana Insect Pest Disease",
    "Banana Healthy Leaf",
    "Banana Bract Mosaic Virus Disease",
    "Banana Black Sigatoka Disease",
  ];

  return (
    <div className="max-w-3xl mx-auto p-6">
      <h2 className="text-3xl font-bold text-black mb-4">เกี่ยวกับแอป 🍌</h2>

      <div className="rounded-2xl border p-6 bg-white shadow-md space-y-4">
        <p className="text-lg text-gray-700 leading-relaxed">
          แอป <span className="font-semibold">DooKluay</span> พัฒนาขึ้นเพื่อช่วยเกษตรกร
          และผู้สนใจตรวจสอบโรคกล้วยผ่าน{" "}
          <span className="font-medium">ภาพถ่ายใบตอง</span> 🌱
        </p>

        <p className="text-gray-700 leading-relaxed">
          ระบบนี้ใช้{" "}
          <span className="font-semibold text-green-700">
            Convolutional Neural Network (CNN)
          </span>{" "}
          ซึ่งเป็นเทคโนโลยี{" "}
          <span className="italic">Deep Learning</span> ด้านการรู้จำภาพ
          ที่สามารถจำแนกอาการของโรคจากภาพใบตองได้อย่างแม่นยำ
        </p>

        <p className="text-gray-700 leading-relaxed">
          โมเดลถูกฝึกให้รู้จักโรคกล้วยที่พบบ่อยทั้งหมด{" "}
          <span className="font-semibold">7 โรค</span> ได้แก่:
        </p>

        <ul className="list-disc list-inside space-y-1 text-gray-700">
          {diseases.map((disease, idx) => (
            <li key={idx} className="ml-2">
              {disease}
            </li>
          ))}
        </ul>

        <p className="text-gray-700 leading-relaxed">
          เพียงคุณอัปโหลดรูปใบตอง ระบบจะ{" "}
          <span className="font-semibold">ทำนายโรคที่เป็นไปได้</span> พร้อม{" "}
          <span className="font-semibold">ระดับความมั่นใจ (%)</span> และ{" "}
          <span className="font-semibold">คำแนะนำเบื้องต้น</span> ในการจัดการโรค
          เพื่อช่วยลดความเสียหายและเพิ่มผลผลิต 🍃
        </p>

        <p className="text-sm text-gray-500 mt-4">
          หมายเหตุ: แอปนี้เป็นเพียงเครื่องมือช่วยเหลือ
          ไม่สามารถใช้แทนการวินิจฉัยโดยผู้เชี่ยวชาญทางการเกษตรได้
        </p>
      </div>
    </div>
  );
}
