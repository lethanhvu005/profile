function youtubeEmbed(value) {
  try {
    const url = new URL(value);
    const host = url.hostname.replace(/^www\./, "");
    let id;
    if (host === "youtu.be") id = url.pathname.slice(1);
    else if (["youtube.com", "m.youtube.com", "youtube-nocookie.com"].includes(host)) {
      id = url.searchParams.get("v");
      if (!id && /^\/(embed|shorts|live)\//.test(url.pathname)) id = url.pathname.split("/")[2];
    }
    return /^[\w-]{11}$/.test(id || "") ? `https://www.youtube-nocookie.com/embed/${id}` : null;
  } catch {
    return null;
  }
}

function ExternalLink({ href, children }) {
  if (!/^https?:\/\//i.test(href || "")) return null;
  return <a className="pill" href={href} target="_blank" rel="noopener noreferrer"><i aria-hidden="true">↗</i>{children}</a>;
}

export default function ProjectDetail({ project }) {
  if (!project) return (
    <section className="page"><div className="content">
      <h1>Không tìm thấy dự án</h1>
      <a className="back-link" href="#projects">← Quay lại dự án</a>
    </div></section>
  );
  const embed = youtubeEmbed(project.youtube_url);
  const technologies = (project.technologies || "").split(",").map((item) => item.trim()).filter(Boolean);
  return (
    <section className="page">
      <article className="content project-detail">
        <a className="back-link" href="#projects">← Tất cả dự án</a>
        <header className="project-heading">
          <p className="kicker">{project.category}{project.is_demo ? " · Dự án minh họa" : ""}</p>
          <h1>{project.title}</h1>
          <p className="body-copy">{project.description}</p>
          {technologies.length > 0 && <div className="tags">{technologies.map((tech, i) => <span key={i}>{tech}</span>)}</div>}
          <div className="actions">
            <ExternalLink href={project.demo_url}>TRẢI NGHIỆM SẢN PHẨM</ExternalLink>
            <ExternalLink href={project.source_url}>GITHUB / SOURCE CODE</ExternalLink>
            <ExternalLink href={project.youtube_url}>DEMO YOUTUBE</ExternalLink>
          </div>
        </header>
        {project.image_url && <img className="project-cover" src={project.image_url} alt={project.title} />}
        {project.content && <section className="detail-section">
          <h2>Thông tin dự án</h2>
          <p className="body-copy project-content">{project.content}</p>
        </section>}
        {project.youtube_url && <section className="detail-section">
          <h2>Video demo sản phẩm</h2>
          {embed && <iframe className="project-video" src={embed} title={`Demo ${project.title}`} loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen />}
          <p className="note">Xem video trên YouTube nếu trình phát không khả dụng.</p>
          <ExternalLink href={project.youtube_url}>XEM TRÊN YOUTUBE</ExternalLink>
        </section>}
        {project.images?.length > 0 && <section className="detail-section">
          <h2>Hình ảnh sản phẩm</h2>
          <div className="project-gallery">
            {project.images.map((item, index) => <figure key={item.id}>
              <a href={item.image_url} target="_blank" rel="noopener noreferrer" aria-label={`Mở ảnh ${index + 1}`}>
                <img src={item.image_url} alt={item.caption || `${project.title} — hình ${index + 1}`} loading="lazy" />
              </a>
              {item.caption && <figcaption>{item.caption}</figcaption>}
            </figure>)}
          </div>
        </section>}
      </article>
    </section>
  );
}
