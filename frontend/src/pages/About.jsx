import { Link } from "react-router-dom";

const skillGroups = [
  {
    title: "Frontend",
    items: [
      "ReactJS (Components, Hooks)",
      "React Router",
      "JavaScript (ES6+)",
      "TypeScript",
      "HTML5 / CSS3",
      "Tailwind CSS",
      "Axios / Fetch API",
      "Responsive UI",
    ],
  },
  {
    title: "Backend",
    items: [
      "Python",
      "Django",
      "Django REST Framework",
      "FastAPI",
      "Flask",
      "RESTful API",
      "Django ORM",
      "SQLAlchemy",
      "JWT & RBAC",
    ],
  },
  {
    title: "Database",
    items: ["PostgreSQL", "SQLite", "SQL"],
  },
  {
    title: "Git & Công cụ",
    items: ["Git", "GitHub", "GitHub Actions", "Postman", "VS Code"],
  },
  {
    title: "Triển khai & Render",
    items: ["Render", "Docker", "Docker Compose", "CI/CD"],
  },
  {
    title: "Sử dụng công cụ AI",
    items: [
      "OpenAI Codex",
      "Antigravity",
      "ChatGPT",
      "GitHub Copilot",
      "Gemini",
      "Cursor",
    ],
  },
];

export default function About({ profile }) {
  return (
    <section className="page" id="about">
      <div className="content">
        <header className="section-head">
          <div className="ghost">ABOUT</div>
          <h2>
            Một chút <em>về mình.</em>
          </h2>
        </header>
        <div className="about-grid">
          <div>
            <div className="kicker">Giới thiệu bản thân</div>
            <h3>
              Lập trình viên Full-stack
              <br />
              Python • Django • ReactJS.
            </h3>
            <p className="body-copy">
              Sinh viên ngành Công nghệ thông tin tại Trường Đại học Công nghệ
              Thông tin và Truyền thông Việt – Hàn (VKU), có kinh nghiệm thực
              hành phát triển ứng dụng Full-stack với Python, Django REST
              Framework, FastAPI, Flask, ReactJS và cơ sở dữ liệu quan hệ.
            </p>
            <p className="body-copy">
              Đã xây dựng nền tảng thương mại điện tử thiết bị gaming (NEXA GEAR
              / CommerceOS) và hệ thống hỗ trợ an toàn lái xe ứng dụng AI
              (SafeVision). Có kiến thức về thiết kế REST API, xác thực JWT,
              tích hợp frontend – backend, giao diện quản trị, thị giác máy tính
              và triển khai ứng dụng. Mong muốn ứng tuyển vị trí Full-stack
              Developer Intern/Fresher.
            </p>
            <div className="facts">
              <div>
                <span>HỌ VÀ TÊN</span>Lê Thành Vũ
              </div>
              <div>
                <span>ĐỊNH HƯỚNG</span>Full-stack Developer
              </div>
              <div>
                <span>HỌC VẤN</span>ĐH Việt – Hàn (VKU)
              </div>
              <div>
                <span>GITHUB</span>
                <a
                  className="fact-link"
                  href="https://github.com/lethanhvu005"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  lethanhvu005 ↗
                </a>
              </div>
            </div>
            <Link className="pill" to="/contact">
              <i>↗</i> KẾT NỐI VỚI MÌNH
            </Link>
          </div>
          <div className="skills">
            <div className="kicker">Kỹ năng chuyên môn</div>
            <h3>Bộ công cụ của mình</h3>
            <p className="body-copy">
              Các công nghệ, cơ sở dữ liệu và quy trình triển khai mình sử dụng
              trong học tập và dự án thực tế.
            </p>
            <div className="skill-groups">
              {skillGroups.map((group) => (
                <div className="skill-group" key={group.title}>
                  <h4>{group.title}</h4>
                  <div className="tags">
                    {group.items.map((item) => (
                      <span key={item}>{item}</span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
        <footer className="foot">
          <span></span>
          <span>01 / ABOUT ME</span>
        </footer>
      </div>
    </section>
  );
}
