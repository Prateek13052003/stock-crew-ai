import axios from "axios";

const api = axios.create({
    baseURL:
        process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000",
});

export default api;

export const downloadPDF = async () => {
    const response = await api.get("/download-pdf", {
        responseType: "blob",
    });

    const url = window.URL.createObjectURL(new Blob([response.data]));

    const link = document.createElement("a");
    link.href = url;
    link.download = "Stock_Report.pdf";

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    window.URL.revokeObjectURL(url);
};