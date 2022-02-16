import React from "react";
import { Spin } from "antd";
import DashboardPage from "./pages/DashboardPage";

const App: React.FC = () => {
  const [isLoading, setIsLoading]: any = React.useState(true);

  const loadStoreData = async () => {
    console.log("Inside Load Data");
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
              <h1>Hello World</h1>
            </div>
          </div>
        </div>
      </main>
    </>
  );
};

export default App;
