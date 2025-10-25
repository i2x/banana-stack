import { Link } from "react-router-dom"

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 text-gray-800 px-4">
      <h1 className="text-6xl font-extrabold text-red-500">404</h1>
      <p className="mt-4 text-2xl font-semibold">Page Not Found</p>
      <p className="mt-2 text-gray-500 text-center">
        ขอโทษครับ ไม่พบหน้าที่คุณกำลังค้นหา 😢
      </p>
      <Link
        to="/"
        className="mt-6 px-6 py-3 bg-blue-600 text-white rounded-xl shadow-lg hover:bg-blue-700 transition"
      >
        กลับหน้าแรก
      </Link>
    </div>
  )
}
