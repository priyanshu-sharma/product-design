import React from "react";
import "antd/dist/antd.min.css";
import "./dashboard-page.css";
import { Layout, Menu, Breadcrumb, PageHeader, Button } from "antd";
import {
  DesktopOutlined,
  PieChartOutlined,
  FileOutlined,
  TeamOutlined,
} from "@ant-design/icons";
import { getImages } from "../../services/api/product-server";
import HandbagPage from "./components/HandbagPage";
import {useState} from 'react';
import Navigation from "./Navigation";

const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;

const DashboardPage: React.FC = () => {
  const [isCollapsed, setIsCollapsed]: any = React.useState(false);

  const onCollapse = () => {
    setIsCollapsed(!isCollapsed);
  };

  const [response, setResponse]:any = useState([])

  const getImpVariables = (
    // responseImage: {
    //   active: boolean;
    //   description: string;
    //   id: number;
    //   meta: number[][];
    //   name: string;
    //   product_id: number;
    //   type: string;
    //   url:string;
    // }[]
    responseImage: {
      id: string;
      url:string;
    }[]
  ) => {
    let imageArray = [];
    for (const image of responseImage) {
      imageArray.push({
        id: image.id,
        path: image.url.substring(70),
      });
    };
    return imageArray;
  }

  const handleApply = async () => {
    console.log("Inside Apply");
    const response = getImpVariables(await getImages());
    console.log(response);
    setResponse(response);
  };

  return (
    <div>
      <Navigation/>
      <Layout style={{ minHeight: "92vh" }}>
        <Layout className="site-layout">
          <Content style={{ margin: "0 16px" }}>
            <Breadcrumb style={{ margin: "16px 0" }}>
              <div
                style={{
                  display: "flex",
                  flexDirection: "row",
                }}
              >
                <div style={{ left: 220, position: "absolute" }}>
                  <Breadcrumb.Item>Handbags</Breadcrumb.Item>
                </div>
                <div style={{ right: 15, position: "absolute" }}>
                  <Button onClick={handleApply}>Generate Images</Button>
                </div>
              </div>
            </Breadcrumb>
            <div
              className="site-layout-background"
              style={{ padding: 30, minHeight: 480 }}
            >
              <HandbagPage images={response}/>
            </div>
          </Content>
        </Layout>
      </Layout>
    </div>
  );
};

export default DashboardPage;
