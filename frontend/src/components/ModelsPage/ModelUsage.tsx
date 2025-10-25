import React, { useState } from "react";

interface ModelUsageProps {
  fileName: string;
}

const ModelUsage: React.FC<ModelUsageProps> = ({ fileName }) => {
  const [isOpen, setIsOpen] = useState(false);

  const code = `import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# โหลดโมเดล
model = load_model("${fileName}.h5")

class_names = [
    "Banana Black Sigatoka Disease",
    "Banana Bract Mosaic Virus Disease",
    "Banana Healthy Leaf",
    "Banana Insect Pest Disease",
    "Banana Moko Disease",
    "Banana Panama Disease",
    "Banana Yellow Sigatoka Disease"
]

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128,128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    preds = model.predict(img_array, verbose=0)
    class_idx = np.argmax(preds)
    return class_names[class_idx]`;

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    alert("Copied ✅");
  };

  return (
    <div className="mt-4 border rounded-lg">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex justify-between items-center px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-t-lg"
      >
        <span className="font-semibold">📖 วิธีใช้งานใน Python</span>
        <span>{isOpen ? "▲" : "▼"}</span>
      </button>

      {isOpen && (
        <div className="relative">
          <pre className="bg-gray-900 text-green-200 text-sm p-4 rounded-b-lg overflow-x-auto">
            {code}
          </pre>
          <button
            onClick={handleCopy}
            className="absolute top-2 right-2 px-3 py-1 bg-blue-600 text-white text-xs rounded hover:bg-blue-700"
          >
            Copy
          </button>
        </div>
      )}
    </div>
  );
};

export default ModelUsage;
