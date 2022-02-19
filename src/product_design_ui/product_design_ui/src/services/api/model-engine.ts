import { httpPost, httpGet, httpPut } from "../http";
import { MODEL_ENGINE_API_URL } from "../constants/api";

const GET = httpGet(MODEL_ENGINE_API_URL);
const POST = httpPost(MODEL_ENGINE_API_URL);
const PUT = httpPut(MODEL_ENGINE_API_URL);


export const getImages = () => {
  return GET("/api/v1/generate_images/", {});
};