import { useState } from "react";

export default function TreatmentCard({
    method,
    source,
}: {
    method?: string;
    source?: string;
}) {
    const [expanded, setExpanded] = useState(false);
    const maxChars = 200;

    if (!method) {
        return (
            <div className="p-4 border rounded-xl bg-white shadow mb-4">
                <p className="text-gray-500">ไม่มีข้อมูลวิธีการรักษา</p>
            </div>
        );
    }

    const displayText =
        !expanded && method.length > maxChars
            ? method.slice(0, maxChars) + "..."
            : method;

    return (
        <div className="p-4 border rounded-xl bg-white shadow mb-4 max-w-full">
            {/* คุมขนาด + ตัดบรรทัด */}
            <p className="whitespace-pre-line break-words text-gray-800">
                {displayText}
            </p>

            {method.length > maxChars && (
                <button
                    onClick={() => setExpanded(!expanded)}
                    className="text-green-600 text-sm mt-2 hover:underline"
                >
                    {expanded ? "ย่อ ▲" : "อ่านต่อ ▼"}
                </button>
            )}

            {source && (
                <a
                    href={source}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block mt-2 text-sm text-blue-600 hover:underline"
                >
                    🔗 แหล่งที่มา
                </a>
            )}
        </div>
    );
}
