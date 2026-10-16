import { useState } from "react";
export default function Projects({ projects }) {
  const [filter, setFilter] = useState("all");
  return (
    <section className="page">
      <div className="content">
        <header className="section-head">
          <div className="ghost">WORK</div>
          <h2>
            Góc <em>dự án.</em>
          </h2>
        </header>
        <div className="filters">
          {[
            ["all", "Tất cả"],
            ["web", "Web"],
            ["mobile", "Mobile"],
            ["ai", "AI"],
          ].map(([id, label]) => (
            <button
              className={filter === id ? "active" : ""}
              key={id}
              onClick={() => setFilter(id)}
            >
              {label}
            </button>
          ))}
        </div>
        <div className="projects">
          {projects
            .filter((p) => filter === "all" || p.category === filter)
            .map((p, i) => (
              <a
                className="project"
                key={p.id}
                href={`#projects/${p.id}`}
              >
                <div
                  className={"art " + ["one", "two", "three", "four"][i % 4]}
                >
                  {p.image_url ? (
                    <img
                      src={p.image_url}
                      alt=""
                      style={{
                        width: "100%",
                        height: "100%",
                        objectFit: "cover",
                      }}
                    />
                  ) : (
                    <div className="mock">
                      <b>{p.title}</b>
                      <p>LEARN. BUILD. EXPLORE.</p>
                      <div className="blocks">
                        <i />
                        <i />
                        <i />
                      </div>
                    </div>
                  )}
                </div>
                <div className="details">
                  <small>
                    {p.category.toUpperCase()}
                    {p.is_demo ? " · MINH HỌA" : ""}
                  </small>
                  <h3>{p.title} ↗</h3>
                  <p>{p.description}</p>
                </div>
              </a>
            ))}
        </div>
        {projects.length === 0 && (
          <p className="body-copy">
            Chưa có dự án. Hãy thêm dự án trong Django Admin.
          </p>
        )}

      </div>
    </section>
  );
}
