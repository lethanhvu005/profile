export default function Contact({ profile }) {
  return (
    <section className="page" id="contact">
      <div className="content">
        <header className="section-head">
          <div className="ghost">HELLO</div>
          <h2>
            Cùng <em>kết nối.</em>
          </h2>
        </header>
        <div className="contact-grid">
          <div>
            <div className="kicker">Bắt đầu một cuộc trò chuyện</div>
            <h3>
              Bạn có một ý tưởng?
              <br />
              Mình rất muốn lắng nghe.
            </h3>
            <p className="body-copy">
              Trao đổi về lập trình, chia sẻ một dự án thú vị hoặc đơn giản là
              gửi một lời chào.
            </p>
            <a
              className="contact-link"
              href="https://github.com/lethanhvu005"
              target="_blank"
              rel="noopener"
            >
              <b>↗</b>
              <div>
                <small>GITHUB</small>
                <span>github.com/lethanhvu005</span>
              </div>
            </a>
            <div className="contact-link">
              <b>@</b>
              <div>
                <small>EMAIL</small>
                <span>{profile.email || "Chưa thêm email liên hệ"}</span>
              </div>
            </div>
            <p className="note">
              Thêm email và mạng xã hội của bạn để hoàn thiện phần liên hệ.
            </p>
          </div>
          <div className="contact-card">
            <div className="monogram">Vũ.</div>
            <h3>
              Thiết kế có chủ đích.
              <br />
              Lập trình bằng sự tò mò.
            </h3>
            <p>Cảm ơn bạn đã ghé thăm không gian cá nhân của mình.</p>
            <a className="pill" href="#projects">
              <i>→</i> KHÁM PHÁ DỰ ÁN
            </a>
          </div>
        </div>
        <footer className="foot">
          <span>© 2026 Lê Thành Vũ</span>
          <span>03 / LET'S CONNECT</span>
        </footer>
      </div>
    </section>
  );
}
