import React from "react";
import { Spin } from "antd";
import DashboardPage from "./pages/DashboardPage";
import { generateImages } from "./services/api/model-engine";

declare global {
  interface Window {
    MODEL_ENGINE_API_URL: string;
    PRODUCT_SERVER_API_URL: string;
  }
}

window.MODEL_ENGINE_API_URL = window.MODEL_ENGINE_API_URL;
window.PRODUCT_SERVER_API_URL = window.PRODUCT_SERVER_API_URL;

const App: React.FC = () => {
  const [isLoading, setIsLoading]: any = React.useState(true);

  const loadStoreData = async () => {
    console.log("Inside Load Data");
    const response = await generateImages();
    console.log(response);
    setIsLoading(false);
  };

  React.useEffect(() => {
    loadStoreData();
  }, []);

  if (isLoading) {
    return <Spin size="large" className="full-page-loader" />;
  }

  return (
    <>
      <main className="main-content">
        <div
          style={{
            flex: 1,
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
          }}
        >
          <div className="body-content">
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
              }}
            >
              <DashboardPage></DashboardPage>
            </div>
          </div>
        </div>
      </main>
    </>
  );
};

export default App;
