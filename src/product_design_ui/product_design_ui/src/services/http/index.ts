const _throwBadResponseError = async (response: Response) => {
    let badResponseError = await response.text();
    if (response.status === 500) {
      badResponseError = "Whoops! Something went wrong.";
    }
    throw new Error(badResponseError);
  };
  
  export const httpGet =
    (host: string) =>
    async (path: string, headers?: any): Promise<any> => {
      const response = await fetch(`${host}${path}`, {
        method: "GET",
        headers: {
          ...headers,
        },
      });
  
      if (!response.ok) {
        await _throwBadResponseError(response);
      }
      return await response.json();
    };
  
  export const httpPut =
    (host: string) =>
    async (path: string, body: any): Promise<any> => {
      const response = await fetch(`${host}${path}`, {
        method: "PUT",
        body: JSON.stringify(body),
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      if (!response.ok) {
        await _throwBadResponseError(response);
      }
  
      return await response.json();
    };
  
  export const httpPost =
    (host: string) =>
    async (
      path: string,
      body: any,
      isFormUpload: boolean = false
    ): Promise<any> => {
      const response = await fetch(`${host}${path}`, {
        method: "POST",
        body: JSON.stringify(body),
        headers: {
          ...(!isFormUpload && { "Content-Type": "application/json" }),
        },
      });
  
      if (!response.ok) {
        await _throwBadResponseError(response);
      }
  
      if (response.headers.get("content-type") == "application/json")
        return await response.json();
  
      return response;
    };
  