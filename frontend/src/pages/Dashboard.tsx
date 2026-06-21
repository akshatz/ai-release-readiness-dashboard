import { useEffect, useState } from "react";

import { api } from "../services/api";

type DashboardData = {

  release_name: string;

  score: number;

  status: string;

  risk: string;

  blockers: string[];

  recommendations: string[];

};

export default function Dashboard() {

  const [data, setData] = useState<DashboardData | null>(null);

  useEffect(() => {

    api.post("/release/readiness", {

      release_name: "Buzz v2.8",

      development_complete: true,

      pr_merged: true,

      staging_deployed: true,

      qa_complete: false,

      release_notes_created: false,

      production_approval: false

    })

    .then((res) => setData(res.data))

    .catch(console.error);

  }, []);

  if (!data) {

    return <h2>Loading...</h2>;

  }

  return (

    <div style={{ padding: "40px" }}>

      <h1>AI Release Readiness Dashboard</h1>

      <hr />

      <ul style={{ textAlign: "left" }}>
        {data.release_name}
      </ul>

      <ul style={{ textAlign: "left" }}>
        Readiness: {data.score}%
      </ul>

      <ul style={{ textAlign: "left" }}>
        Status: {data.status}
      </ul>

      <ul style={{ textAlign: "left" }}>
        Risk: {data.risk}
      </ul>

      <ul style={{ textAlign: "left" }}>
        Blockers
      </ul>

      <ul style={{ textAlign: "left" }}>

        {data.blockers.map((blocker) => (

          <li key={blocker}>{blocker}</li>

          )
        )
      }

      </ul>

      <ul style={{ textAlign: "left" }}>
        Recommendations
      </ul>

      <ul style={{ textAlign: "left" }}>

      {data.recommendations.map((recommemndation) => (

        <li key={recommemndation}>{recommemndation}</li>

      ))}

      </ul>

    </div>

  );

}
