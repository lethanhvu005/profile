import { useEffect, useState } from "react";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Projects from "./pages/Projects";
import ProjectDetail from "./pages/ProjectDetail";
const ids = ["home", "about", "projects", "contact"],
  labels = ["Trang chủ", "Giới thiệu", "Dự án", "Liên hệ"],
  symbols = [
    <>
      <path d="m3 10 9-7 9 7" />
      <path d="M5 9v12h14V9M9 21v-7h6v7" />
    </>,
    <>
      <circle cx="12" cy="7" r="4" />
      <path d="M4 21v-3a8 8 0 0 1 16 0v3" />
    </>,
    <>
      <rect x="3" y="7" width="18" height="14" rx="2" />
      <path d="M8 7V3h8v4M3 13h18" />
    </>,
    <>
      <rect x="3" y="5" width="18" height="14" rx="2" />
      <path d="m3 6 9 7 9-7" />
    </>,
  ];
export default function App() {
  const [page, setPage] = useState(location.hash.slice(1) || "home");
  const activePage = page.startsWith("projects/") ? "projects" : page;
  const [light, setLight] = useState(
    localStorage.getItem("vu-theme") === "light",
  );
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  useEffect(() => {
    const f = () => {
      setPage(location.hash.slice(1) || "home");
      window.scrollTo(0, 0);
    };
    addEventListener("hashchange", f);
    return () => removeEventListener("hashchange", f);
  }, []);
  useEffect(() => {
    document.body.classList.toggle("light", light);
    localStorage.setItem("vu-theme", light ? "light" : "dark");
  }, [light]);
  useEffect(() => {
    const c = new AbortController();
    fetch("/api/portfolio/", { signal: c.signal })
      .then((r) => {
        if (!r.ok) throw Error("Không tải được dữ liệu");
        return r.json();
      })
      .then(setData)
      .catch((e) => {
        if (e.name !== "AbortError")
          setError(
            "Không kết nối được Django. Hãy chạy backend trên cổng 8000 và tải lại trang.",
          );
      });
    return () => c.abort();
  }, []);
  return (
    <>
      <a className="brand" href="#home">
        Thành Vũ<span></span>
      </a>
      <button
        className="theme"
        aria-label={light ? "Chuyển sang giao diện tối" : "Chuyển sang giao diện sáng"}
        aria-pressed={light}
        onClick={() => setLight(!light)}
      >
        <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true">
          {light ? <path fill="currentColor" d="M20.8 14.1A9 9 0 0 1 9.9 3.2 9 9 0 1 0 20.8 14.1Z" /> : <>
            <circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" strokeWidth="2" />
            <path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
          </>}
        </svg>
      </button>
      <nav className="nav" aria-label="Điều hướng">
        {ids.map((id, i) => (
          <button
            key={id}
            className={activePage === id ? "active" : ""}
            onClick={() => (location.hash = id)}
            aria-label={labels[i]}
            aria-current={activePage === id ? "page" : undefined}
          >
            <span>{labels[i]}</span>
            <svg viewBox="0 0 24 24" aria-hidden="true">
              {symbols[i]}
            </svg>
          </button>
        ))}
      </nav>
      <main>
        {error ? (
          <div className="content">
            <p className="error">{error}</p>
            <button onClick={() => location.reload()}>Thử lại</button>
          </div>
        ) : !data ? (
          <div className="content">Đang tải portfolio…</div>
        ) : page === "about" ? (
          <About profile={data.profile} />
        ) : page === "contact" ? (
          <Contact profile={data.profile} />
        ) : page.startsWith("projects/") ? (
          <ProjectDetail project={data.projects.find((p) => String(p.id) === page.slice(9))} />
        ) : page === "projects" ? (
          <Projects projects={data.projects} />
        ) : (
          <Home profile={data.profile} />
        )}
      </main>
    </>
  );
}
