import React from "react";
import "antd/dist/antd.css";
import "./dashboard-page.css";
import { Layout, Menu, Breadcrumb, PageHeader } from "antd";
import {
  DesktopOutlined,
  PieChartOutlined,
  FileOutlined,
  TeamOutlined,
} from "@ant-design/icons";

const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;

const DashboardPage: React.FC = () => {
  const [isCollapsed, setIsCollapsed]: any = React.useState(false);

  const onCollapse = () => {
    setIsCollapsed(!isCollapsed);
  };

  return (
    <div>
      <PageHeader
        title="Product Design"
        className="site-page-header"
        avatar={{
          src: "https://avatars1.githubusercontent.com/u/8186664?s=460&v=4",
        }}
      ></PageHeader>
      <Layout style={{ minHeight: "92vh" }}>
        <Sider collapsible collapsed={isCollapsed} onCollapse={onCollapse}>
          <Menu theme="dark" defaultSelectedKeys={["1"]} mode="inline">
            <Menu.Item key="1" icon={<PieChartOutlined />}>
              Handbags
            </Menu.Item>
            <Menu.Item key="2" icon={<DesktopOutlined />}>
              T-Shirts
            </Menu.Item>
            <Menu.Item key="3" icon={<FileOutlined />}>
              Jeans
            </Menu.Item>
            <Menu.Item key="4" icon={<TeamOutlined />}>
              Jewellary
            </Menu.Item>
          </Menu>
        </Sider>
        <Layout className="site-layout">
          <Content style={{ margin: "0 16px" }}>
            <Breadcrumb style={{ margin: "16px 0" }}>
              <Breadcrumb.Item>Handbags</Breadcrumb.Item>
              <Breadcrumb.Item>Dataset</Breadcrumb.Item>
            </Breadcrumb>
            <div
              className="site-layout-background"
              style={{ padding: 24, minHeight: 360 }}
            >
              Hello World
            </div>
          </Content>
          <Footer style={{ textAlign: "center" }}>
            Product Design ©2022 Created by Priyanshu Sharma
          </Footer>
        </Layout>
      </Layout>
    </div>
  );
};

export default DashboardPage;
