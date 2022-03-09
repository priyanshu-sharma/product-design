import { httpPost, httpGet, httpPut } from "../http";
import { PRODUCT_SERVER_API_URL } from "../constants/api";

const GET = httpGet(PRODUCT_SERVER_API_URL);
const POST = httpPost(PRODUCT_SERVER_API_URL);
const PUT = httpPut(PRODUCT_SERVER_API_URL);

export const getImages = () => {
  return GET("/api/product_domain/v1/handbag_detail/?limit=100");
};
