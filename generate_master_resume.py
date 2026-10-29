#!/usr/bin/env python3
import sys
import os
from PySide6.QtGui import QTextDocument, QPdfWriter, QPageLayout, QPageSize
from PySide6.QtCore import QSizeF, QMarginsF
from PySide6.QtWidgets import QApplication

def generate_master_resume_html():
    html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    font-size: 7.7pt;
    line-height: 1.17;
    background: #ffffff;
  }
  
  /* Header */
  .header {
    text-align: center;
    padding-bottom: 2px;
    border-bottom: 1.8px solid #0f172a;
    margin-bottom: 3.5px;
  }
  .name {
    font-size: 16.5pt;
    font-weight: 800;
    letter-spacing: 0.6px;
    color: #0f172a;
    text-transform: uppercase;
    margin-bottom: 1px;
  }
  .title {
    font-size: 9.0pt;
    font-weight: 700;
    color: #0284c7;
    letter-spacing: 0.3px;
    margin-bottom: 1px;
  }
  .subtitle {
    font-size: 7.4pt;
    font-weight: 500;
    color: #64748b;
    margin-bottom: 2.5px;
  }
  .contact-line1 {
    font-size: 7.6pt;
    color: #475569;
    margin-bottom: 1px;
  }
  .contact-line2 {
    font-size: 7.3pt;
    color: #475569;
  }
  .contact-line2 a, .contact-line1 a {
    color: #0284c7;
    text-decoration: none;
  }
  .sep {
    color: #94a3b8;
    margin: 0 4px;
  }

  /* Parent Section Headings */
  .section {
    margin-bottom: 2.8px;
  }
  .section-header-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 2.0px;
  }
  .section-title-cell {
    font-size: 8.5pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #0f172a;
    border-bottom: 1.4px solid #0284c7;
    padding-bottom: 1.2px;
  }
  .stage-tag {
    font-size: 7.6pt;
    font-weight: 600;
    color: #0284c7;
    text-transform: none;
    letter-spacing: normal;
  }

  /* Summary */
  .summary-text {
    font-size: 7.6pt;
    color: #334155;
    line-height: 1.17;
    text-align: justify;
  }

  /* Skills Matrix */
  .skills-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
  }
  .skills-table td {
    padding: 0.25px 0;
    vertical-align: top;
  }
  .skill-category {
    font-weight: 700;
    color: #0369a1; /* Distinct Deep Ocean Blue */
    width: 21%;
    white-space: nowrap;
  }
  .skill-items {
    color: #334155;
    width: 79%;
  }

  /* Experience & Projects */
  .entry {
    margin-bottom: 3.0px;
  }
  .entry-header {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 0px;
  }
  .entry-title {
    text-align: left;
    width: 80%;
    border-left: 2.8px solid #0284c7;
    padding-left: 4.5px;
  }
  .company-name, .project-name {
    font-weight: 800;
    font-size: 8.0pt;
    color: #0f172a;
  }
  .role-title, .project-desc {
    font-weight: 600;
    font-size: 7.7pt;
    color: #0284c7;
  }
  .entry-date {
    font-size: 7.4pt;
    color: #64748b;
    text-align: right;
    font-weight: 500;
    white-space: nowrap;
    width: 20%;
  }
  .entry-meta {
    font-size: 7.2pt;
    color: #475569;
    font-style: italic;
    margin-top: 0.8px;
    margin-bottom: 0.8px;
  }

  /* Bullet Table */
  .bullet-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.2px;
  }
  .bullet-table td {
    vertical-align: top;
    padding: 0.2px 0;
    font-size: 7.5pt;
    line-height: 1.17;
    color: #334155;
  }
  .bullet-dot {
    width: 11px;
    color: #0284c7;
    font-weight: bold;
    text-align: left;
  }
  .bullet-text b {
    color: #0f172a;
  }

  /* Education & Certs Row */
  .two-col {
    width: 100%;
    border-collapse: collapse;
  }
  .two-col td {
    vertical-align: top;
    width: 50%;
  }
  .col-left {
    padding-right: 8px;
  }
  .col-right {
    padding-left: 8px;
  }
  
  .page-divider {
    page-break-before: always;
  }
</style>
</head>
<body>

  <!-- ==================== PAGE 1 ==================== -->

  <!-- HEADER -->
  <div class="header">
    <div class="name">NASIR HAYAT</div>
    <div class="title">DEVOPS &amp; DEVSECOPS ENGINEER</div>
    <div class="subtitle">Cloud-Native Infrastructure &bull; CI/CD &amp; Security Automation &bull; Full-Stack &amp; AI Systems</div>
    <div class="contact-line1">
      <span>Peshawar, Pakistan</span>
      <span class="sep">|</span>
      <span>+92 333 9495197</span>
    </div>
    <div class="contact-line2">
      <a href="mailto:nasirhayat.dev@gmail.com">nasirhayat.dev@gmail.com</a>
      <span class="sep">|</span>
      <a href="https://www.linkedin.com/in/nasir-hayat-4515202a2">linkedin.com/in/nasir-hayat-4515202a2</a>
      <span class="sep">|</span>
      <a href="https://github.com/nasirhayat028">github.com/nasirhayat028</a>
    </div>
  </div>

  <!-- PROFESSIONAL SUMMARY -->
  <div class="section">
    <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
      <tr><td class="section-title-cell">Professional Summary</td></tr>
    </table>
    <div class="summary-text">
      DevOps &amp; DevSecOps Engineer skilled in automating CI/CD pipelines, securing cloud-native infrastructure, and managing Kubernetes workloads. Hands-on experience integrating shift-left security (SAST, secrets detection, container scanning, and DAST) and declarative GitOps with Argo CD. Experienced in Linux administration, AWS cloud services, and secure containerized deployments.
    </div>
  </div>

  <!-- TECHNICAL SKILLS -->
  <div class="section">
    <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
      <tr><td class="section-title-cell">Technical Skills</td></tr>
    </table>
    <table class="skills-table" width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td class="skill-category">DevSecOps &amp; CI/CD:</td>
        <td class="skill-items">GitHub Actions, Argo CD (Declarative GitOps), Jenkins &amp; Groovy Shared Libraries, Docker Hub, Gitleaks, Trivy (Container CVEs), SonarQube (SAST), OWASP ZAP (DAST), npm audit, CSP &amp; Security Headers</td>
      </tr>
      <tr>
        <td class="skill-category">Cloud &amp; Orchestration:</td>
        <td class="skill-items">Kubernetes (kind, Namespaces, Pods, Deployments, Services, ConfigMaps, Secrets, NGINX Ingress, NetworkPolicies, Limits/Quotas, PDB), AWS (EC2, S3, IAM, VPC, CloudWatch, ECR), Linux (Bash CLI, Systemd, Network Troubleshooting)</td>
      </tr>
      <tr>
        <td class="skill-category">Full-Stack &amp; Systems:</td>
        <td class="skill-items">TypeScript, JavaScript, Node.js, Express.js, React, Vite, Tailwind CSS, PostgreSQL, MongoDB, RESTful APIs, Golang (foundations)</td>
      </tr>
      <tr>
        <td class="skill-category">Mobile &amp; AI Engineering:</td>
        <td class="skill-items">Kotlin, Android Jetpack Compose, Hilt DI, Firebase (Auth/Firestore/Storage), Chrome Extensions (Manifest V3), Multi-LLM API Orchestration (OpenAI, Claude, Gemini), Autonomous Agent Workflows</td>
      </tr>
      <tr>
        <td class="skill-category">Observability &amp; Testing:</td>
        <td class="skill-items">Prometheus, Grafana, Vitest, Supertest, Playwright (E2E &amp; Accessibility testing), axe-core</td>
      </tr>
    </table>
  </div>

  <!-- WORK EXPERIENCE -->
  <div class="section">
    <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
      <tr><td class="section-title-cell">Professional Work Experience</td></tr>
    </table>

    <!-- Internship 1 -->
    <div class="entry">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="company-name">CodeOps Pro</span> <span class="role-title">&ndash; DevOps Engineering Intern</span></td>
          <td class="entry-date">2026 (Remote)</td>
        </tr>
      </table>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Containerized multi-tier applications using <b>Docker</b> and multi-stage builds, standardizing development environments and deployment consistency.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Configured <b>Kubernetes</b> workloads (Deployments, ClusterIP/NodePort Services, ConfigMaps, Secrets) and deployed <b>Prometheus &amp; Grafana</b> monitoring stacks for container performance visibility.</td>
        </tr>
      </table>
    </div>

    <!-- Internship 2 -->
    <div class="entry" style="margin-top: 5.5px;">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="company-name">Rhombix Technologies</span> <span class="role-title">&ndash; DevOps &amp; Linux Intern</span></td>
          <td class="entry-date">2026 (Remote)</td>
        </tr>
      </table>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Automated Linux system administration tasks, user permissions, and directory structures across Ubuntu environments via modular <b>Bash scripting</b>.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Monitored system processes, memory/disk utilization, and network sockets using native Linux CLI tooling, optimizing package management and system stability.</td>
        </tr>
      </table>
    </div>
  </div>

  <!-- STAGE 1 (FLAGSHIP) ON PAGE 1 -->
  <div class="section">
    <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
      <tr><td class="section-title-cell">Featured Projects &bull; <span class="stage-tag">Stage 1: DevSecOps &amp; Cloud-Native Platforms</span></td></tr>
    </table>

    <!-- Flagship Project -->
    <div class="entry">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="project-name">End-to-End DevSecOps Delivery Pipeline</span> <span class="project-desc">&ndash; Kubernetes GitOps Platform</span></td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">GitHub Actions, Docker, Kubernetes (kind), Argo CD, NGINX Ingress, Trivy, SonarQube, Gitleaks, OWASP ZAP, Vitest, Node.js</div>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Automated CI/CD Delivery:</b> Built automated GitHub Actions pipeline executing unit and integration tests, creating version-tagged Docker images (<code>build-&lt;num&gt;</code>) pushed to Docker Hub.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Shift-Left Security Architecture:</b> Integrated 4-tier security barrier into CI: <b>Gitleaks</b> (credentials detection), <b>npm audit</b> (dependency gating), <b>SonarQube</b> (code quality), and <b>Trivy</b> (container vulnerability triage).</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>GitOps &amp; DAST Hardening:</b> Reconciled desired Kubernetes states via <b>Argo CD</b> on a multi-node <b>kind</b> cluster; routed traffic via <b>NGINX Ingress</b> and executed containerized <b>OWASP ZAP</b> scans with strict CSP and HTTP security response headers.</td>
        </tr>
      </table>
    </div>
  </div>

  <!-- ==================== PAGE 2 ==================== -->
  <div class="page-divider"></div>

  <!-- STAGE 1 (CONT.): DEVTRACK PMS & JENKINS -->
  <div class="section">
    <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
      <tr><td class="section-title-cell">Featured Projects &bull; <span class="stage-tag">Stage 1 (Cont.): Cloud-Native Hardening &amp; Reusable CI/CD</span></td></tr>
    </table>

    <!-- DevTrack PMS -->
    <div class="entry">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="project-name">DevTrack PMS</span> <span class="project-desc">&ndash; Full-Stack App &amp; K8s Hardening</span></td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">React, Vite, Node.js, Express, MongoDB, Docker, Kubernetes NetworkPolicies, LimitRanges, PriorityClasses, PDB</div>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Security Hardening &amp; Microsegmentation:</b> Authored Kubernetes <b>NetworkPolicies</b> restricting MongoDB ingress exclusively to authorized backend pods, preventing lateral container network access.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Resource Governance &amp; Multi-stage Builds:</b> Implemented <b>LimitRanges</b>, resource quotas, <b>PriorityClasses</b>, and <b>PodDisruptionBudgets (PDB)</b>; created multi-stage alpine Dockerfiles running as non-root user (<code>nasir</code>).</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>High Availability &amp; Lifecycle Operations:</b> Configured readiness/liveness probes, health checks, and rolling update strategies ensuring seamless zero-downtime container lifecycles.</td>
        </tr>
      </table>
    </div>

    <!-- Jenkins Shared Libraries -->
    <div class="entry" style="margin-top: 5.0px;">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="project-name">Jenkins Enterprise Shared Libraries</span> <span class="project-desc">&ndash; Reusable CI/CD Automation</span></td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">Groovy, Jenkins Pipeline, Git, Docker, Automation Architecture</div>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Standardized Pipeline Architecture:</b> Developed modular, reusable Jenkins shared libraries (<code>vars/</code>) standardizing build, test, Docker publishing, and deployment workflows across repositories.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>CI/CD Best Practices:</b> Built parameter-driven stages, environment-agnostic steps, and error handling mechanisms to streamline developer onboarding and pipeline maintainability.</td>
        </tr>
      </table>
    </div>
  </div>

  <!-- STAGE 2: AI AUTOMATION, MOBILE & SYSTEMS -->
  <div class="section">
    <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
      <tr><td class="section-title-cell">Featured Projects &bull; <span class="stage-tag">Stage 2: AI Automation, Mobile &amp; Systems Architecture</span></td></tr>
    </table>

    <!-- Social Media Agent -->
    <div class="entry">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="project-name">Social Media Automation Agent</span> <span class="project-desc">&ndash; Multi-Platform Content Workflow</span></td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">Python, Multi-Agent Architecture, API Integration, Automation Pipeline</div>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Autonomous Workflow Pipeline:</b> Architected an automated agent pipeline for multi-platform content planning, automated drafting, and cross-platform formatting (LinkedIn, YouTube, Instagram) with human-in-the-loop verification.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Resilience &amp; Error Recovery:</b> Implemented rate-limiting recovery, structured schema validation, and persistent execution state for uninterrupted autonomous tasks.</td>
        </tr>
      </table>
    </div>

    <!-- AI MCQ Project -->
    <div class="entry" style="margin-top: 5.0px;">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="project-name">Multi-Model AI Consensus Engine</span> <span class="project-desc">&ndash; Browser Extension</span></td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">Chrome Manifest V3, TypeScript, React, OpenAI API, Anthropic Claude API, Google Gemini API</div>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Multi-LLM Orchestration:</b> Architected Chrome extension comparing responses across OpenAI, Gemini, and Claude models to surface agreement, variance, and uncertainty signals with secure client-side API key isolation.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Security &amp; Extensibility:</b> Built clean provider abstraction layers with schema validation and strict adherence to Manifest V3 security requirements.</td>
        </tr>
      </table>
    </div>

    <!-- TeamSyncAI -->
    <div class="entry" style="margin-top: 5.0px;">
      <table class="entry-header" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="entry-title"><span class="project-name">TeamSyncAI</span> <span class="project-desc">&ndash; Android Collaboration &amp; Workspace Platform</span></td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">Kotlin, Jetpack Compose, Hilt DI, Firebase Auth/Firestore/Storage, Unit Testing, ProGuard/R8</div>
      <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Native Android Architecture &amp; RBAC:</b> Designed scalable collaboration platform with multi-tenant workspace isolation, role-based access control (Owner, Admin, Manager, Employee), real-time chat, and attendance tracking.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Reliability, Security &amp; Hardening:</b> Maintained high software quality with <b>19/19 passing automated unit tests</b>, strict MVVM separation, verified release/R8 obfuscation, and fine-grained Firebase security rules.</td>
        </tr>
      </table>
    </div>
  </div>

  <!-- EDUCATION & CERTIFICATIONS (2 COLUMNS) -->
  <div class="section">
    <table class="two-col" width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td class="col-left">
          <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
            <tr><td class="section-title-cell">Education</td></tr>
          </table>
          <div class="entry">
            <div class="entry-title" style="width: 100%;"><span class="company-name">Kohat University of Science &amp; Technology (KUST)</span></div>
            <div class="entry-subtitle" style="color: #334155; font-weight: 500; font-size: 7.7pt;">BS in Computer Science</div>
            <div class="entry-date" style="text-align: left; margin-top: 1px;">2023 &ndash; 2027</div>
            <div class="entry-meta" style="margin-top: 1px;">Coursework: Distributed Systems, Operating Systems, Computer Networks, Database Systems, Software Engineering</div>
          </div>
        </td>
        <td class="col-right">
          <table class="section-header-table" width="100%" cellpadding="0" cellspacing="0">
            <tr><td class="section-title-cell">Certifications &amp; Programs</td></tr>
          </table>
          <div class="entry">
            <table class="bullet-table" width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td class="bullet-dot">&bull;</td>
                <td class="bullet-text"><b>AWS re/Start Graduate / Coursework</b><br><span style="font-size: 7.2pt; color: #64748b;">Cloud Architecture, EC2, S3, IAM, VPC, Linux Administration, Networking &amp; Security</span></td>
              </tr>
              <tr>
                <td class="bullet-dot">&bull;</td>
                <td class="bullet-text"><b>AWS DevOps Engineering Program</b><br><span style="font-size: 7.2pt; color: #64748b;">Cloud CI/CD Automation, Infrastructure as Code &amp; Scalable Delivery</span></td>
              </tr>
            </table>
          </div>
        </td>
      </tr>
    </table>
  </div>

</body>
</html>
"""
    return html_content

def build_pdf():
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    app = QApplication.instance() or QApplication(sys.argv)
    
    html = generate_master_resume_html()
    
    # Save HTML file
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(repo_dir, "Nasir_Hayat_Master_Resume.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved HTML to {html_path}")

    # Write PDF
    pdf_path = os.path.join(repo_dir, "Nasir_Hayat_Master_Resume.pdf")
    doc = QTextDocument()
    doc.setDocumentMargin(0)
    
    writer = QPdfWriter(pdf_path)
    writer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
    
    # Margins: 5.5mm top/bottom, 8mm left/right
    layout = QPageLayout(
        QPageSize(QPageSize.PageSizeId.A4),
        QPageLayout.Orientation.Portrait,
        QMarginsF(8, 5.5, 8, 5.5),
        QPageLayout.Unit.Millimeter
    )
    writer.setPageLayout(layout)
    
    paint_size = layout.paintRectPoints()
    doc.setPageSize(QSizeF(paint_size.width(), paint_size.height()))
    doc.setHtml(html)
    page_count = doc.pageCount()
    print("Pre-print doc pageCount:", page_count)
    doc.print_(writer)
    print(f"Saved PDF to {pdf_path}")
    return page_count

if __name__ == "__main__":
    build_pdf()
