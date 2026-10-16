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
            <div className="kicker">Không ngừng học hỏi</div>
            <h3>
              Từ một ý tưởng nhỏ,
              <br />
              đến một sản phẩm có ích.
            </h3>
            <p className="body-copy">
              Mình là Vũ, một sinh viên yêu thích lập trình web. Mình đang tìm
              hiểu cách kết hợp giao diện dễ sử dụng với hệ thống hoạt động rõ
              ràng, hiệu quả.
            </p>
            <p className="body-copy">
              ReactJS, Python và Django là những công nghệ mình quan tâm. Mỗi dự
              án là một cơ hội để thực hành, thử nghiệm và hiểu sâu hơn về cách
              xây dựng phần mềm.
            </p>
            <div className="facts">
              <div>
                <span>HỌ VÀ TÊN</span>Lê Thanh Vũ
              </div>
              <div>
                <span>ĐỊNH HƯỚNG</span>Web Development
              </div>
              <div>
                <span>NGÔN NGỮ</span>Tiếng Việt
              </div>
              <div>
                <span>GITHUB</span>lethanhvu005
              </div>
            </div>
            <a className="pill" href="#contact">
              <i>↗</i> KẾT NỐI VỚI MÌNH
            </a>
          </div>
          <div className="skills">
            <div className="kicker">Công nghệ quan tâm</div>
            <h3>Bộ công cụ của mình</h3>
            <p className="body-copy">
              Những công nghệ mình đang học và sử dụng trong các bài thực hành.
            </p>
            <div className="tags">
              <span>ReactJS</span>
              <span>JavaScript</span>
              <span>HTML / CSS</span>
              <span>Python</span>
              <span>Django</span>
              <span>MongoDB</span>
              <span>React Native</span>
              <span>Git / GitHub</span>
            </div>
            <div className="divider"></div>
            <h3>Học bằng cách làm.</h3>
            <p className="body-copy">
              Từ ứng dụng di động đến website và các ý tưởng AI — mình thích thử
              sức với những bài toán mới.
            </p>
          </div>
        </div>
        <footer className="foot">
          <span>Ít hơn, nhưng chỉn chu hơn.</span>
          <span>01 / ABOUT ME</span>
        </footer>
      </div>
    </section>
  );
}
