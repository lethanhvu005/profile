export default function Home({ profile }) {
  return (
    <section className="page" id="home">
      <div className="hero">
        <div className="wedge"></div>
        <div
          className="portrait"
          role="img"
          aria-label="Minh họa chân dung, có thể thay bằng ảnh cá nhân"
        >
          <small>PERSONAL PORTFOLIO</small>
          {profile.image_url ? (
            <img src={profile.image_url} alt={profile.name} />
          ) : (
            <svg viewBox="0 0 350 520" fill="none">
              <ellipse cx="180" cy="510" rx="150" ry="190" fill="#172321" />
              <path d="M118 310h112l30 100-80 70-85-70z" fill="#243632" />
              <path d="M145 265h65v79l-32 30-33-31z" fill="#a58d75" />
              <ellipse cx="177" cy="202" rx="72" ry="91" fill="#baa088" />
              <path
                d="M105 207c-17-79 20-120 74-120 63 0 90 49 68 120l-19-62c-40 18-74 12-93 0l-13 65z"
                fill="#1c211f"
              />
              <path
                d="M111 202h59m15 0h58m-73 0h15"
                stroke="#262a26"
                strokeWidth="7"
              />
              <rect
                x="118"
                y="188"
                width="51"
                height="32"
                rx="10"
                stroke="#262a26"
                strokeWidth="5"
              />
              <rect
                x="186"
                y="188"
                width="51"
                height="32"
                rx="10"
                stroke="#262a26"
                strokeWidth="5"
              />
              <path d="M162 247q17 9 33-1" stroke="#806a57" strokeWidth="3" />
              <path
                d="M105 360l73 58 72-58M178 420v100"
                stroke="#40514a"
                strokeWidth="3"
              />
            </svg>
          )}
          <div className="cap">YOUR NEXT CHAPTER STARTS HERE</div>
        </div>
        <div className="intro">
          <div className="eyebrow">
            <span className="dot"></span> Xin chào, rất vui được gặp bạn
          </div>
          <h1>
            <span>Mình là {profile.name}.</span>
            <br />
            {profile.role}
          </h1>
          <p>{profile.bio}</p>
          <div className="actions">
            <a className="pill" href="#about">
              <i>→</i> VỀ MÌNH
            </a>
            <a className="pill" href="#projects">
              <i>↗</i> XEM DỰ ÁN
            </a>
          </div>
        </div>
        <div className="hero-footer">
          <a
            href="https://github.com/lethanhvu005"
            target="_blank"
            rel="noopener"
          >
            GITHUB ↗
          </a>
          　 /　 DESIGN · CODE · CREATE
        </div>
      </div>
    </section>
  );
}
