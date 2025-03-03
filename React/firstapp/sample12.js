import { useState } from "react";

export default function SimpleWebPage() {
  const [message, setMessage] = useState("Welcome to My Simple React Page!");

  const handleClick = () => {
    setMessage("You clicked the button!");
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-2xl shadow-lg text-center">
        <h1 className="text-3xl font-bold mb-4 text-blue-600">Simple React Page</h1>
        <p className="text-lg text-gray-700 mb-4">{message}</p>
        <button
          className="px-6 py-2 bg-blue-500 text-white rounded-xl hover:bg-blue-600 transition"
          onClick={handleClic
            k}
        >
          Click Me
        </button>
      </div>
    </div>
  );
}
