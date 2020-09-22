using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PBI_REST_Sample
{
    class SQLHelper
    {
        private SqlConnection conn;
        public SQLHelper()
        {
            conn = new SqlConnection("data source=Ignitiondata;initial catalog =BAGAIData_PPE; persist security info = True;Integrated Security = SSPI;");
            conn.Open();
        }

        public List<string> GetGroups()
        {
            SqlCommand sqlCommand = new SqlCommand("SELECT * FROM tblPowerBIGroup  where isadmin=1 and id not in (select groupid from tblPowerBIDatasets)", conn);
            SqlDataReader reader = sqlCommand.ExecuteReader();
            List<string> lst = new List<string>() ;
            while (reader.Read())
            {
                lst.Add(reader[0].ToString());
            }
            reader.Close();
            return lst;
        }
        public void insert(string id, string ds, string rpt, string db)
        {
            using (SqlCommand sqlCommand = new SqlCommand($"INSERT INTO tblPowerBIDatasets VALUES('{id}','{ds}','{rpt}','{db}')", conn))
                sqlCommand.ExecuteNonQuery();
        }

        public void insert(string grp)
        {
            using (SqlCommand sqlCommand = new SqlCommand($"INSERT INTO tblPowerBIGrps VALUES('{grp}')", conn))
                sqlCommand.ExecuteNonQuery();
        }

        public void close()
        {
            conn.Close();
        }
    }
}
