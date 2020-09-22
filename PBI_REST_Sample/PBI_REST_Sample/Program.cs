using Microsoft.IdentityModel.Clients.ActiveDirectory;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections;
using System.IO;
using System.Net;
using System.Threading.Tasks;
using System.Configuration;
using System.Threading;

namespace PBI_REST_Sample
{
    class Dataset
    {
        public string id { get; set; }
        public string name { get; set; }
        public string configuredBy { get; set; }
        public Boolean isRefreshable { get; set; }

        public override string ToString()
        {
            return $"Id: {id},\nName: {name}\nconfiguredBy: {configuredBy}\nisRefreshable: {isRefreshable}\n";

        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            DoSync(null);
        }
        static void DoSync(string[] args)
        {
            //SQLHelper sql = new SQLHelper();
            //var pbiGroups = sql.GetGroups();
            //sql.close();

            //string grp = $"https://api.powerbi.com/v1.0/myorg/groups/";   

            string ds = $"https://api.powerbi.com/v1.0/myorg/groups/692b827d-37bd-48f7-bf8b-268b19ae2c8c/datasets";

            JToken dsvalues = InvokeRestAPI(ds);
            /*
            int i = 0;
            foreach (var groupId in pbiGroups)
            {
                SQLHelper sql1 = new SQLHelper();

                Console.WriteLine($"Reading {i++} - {groupId}");

                string ds = $"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets";
                string db = $"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/dashboards";
                string rpt = $"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports";

                JToken dsvalues = InvokeRestAPI(ds);
                JToken dbvalues = InvokeRestAPI(db);
                JToken rptvalues = InvokeRestAPI(rpt);

                sql1.insert(groupId, dsvalues.ToString(), rptvalues.ToString(), dbvalues.ToString());
                sql1.close();

                Thread.Sleep(50000);
            }
            */

            Console.ReadLine();
        }

        private static JToken InvokeRestAPI(string apiEndpoint)
        {
            HttpWebRequest request = WebRequest.Create(apiEndpoint) as HttpWebRequest;

            var token = GetToken().Result;

            request.KeepAlive = true;
            request.Method = "GET";
            request.Headers.Add("Authorization", String.Format("Bearer {0}", token));

            var response = (HttpWebResponse)request.GetResponse();

            var responseBody = new StreamReader(response.GetResponseStream()).ReadToEnd();
            var values = JObject.Parse(responseBody)["value"];
            return values;
        }

        // TODO: Install-Package Microsoft.IdentityModel.Clients.ActiveDirectory -Version 2.21.301221612
        private static async Task<string> GetToken()
        {
            var appSettings = ConfigurationManager.AppSettings;
            
            string clientID = appSettings["ClientId"].ToString();  //App Id of registered your client app.
            
            string AADUserId = appSettings["AADUserId"].ToString();
            string AADKey = appSettings["AADPassword"].ToString();

            string authorityUri = "https://login.windows.net/common/oauth2/authorize";
            AuthenticationContext authContext = new AuthenticationContext(authorityUri);

            UserPasswordCredential creds = new UserPasswordCredential(AADUserId, AADKey);

            string resourceUri = "https://analysis.windows.net/powerbi/api";
            AuthenticationResult result = await authContext.AcquireTokenAsync(resourceUri, clientID, creds);
            
            return result.AccessToken;
        }
    }
}