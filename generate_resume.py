#!/usr/bin/env python3
import sys
import os
import glob
from PySide6.QtGui import QTextDocument, QPdfWriter, QPageLayout, QPageSize
from PySide6.QtCore import QSizeF, QMarginsF
from PySide6.QtWidgets import QApplication

def generate_resume_html():
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
    font-size: 8.2pt;
    line-height: 1.25;
    background: #ffffff;
  }
  
  /* Header */
  .header {
    text-align: center;
    padding-bottom: 4px;
    border-bottom: 2px solid #0f172a;
    margin-bottom: 6px;
  }
  .name {
    font-size: 18pt;
    font-weight: 800;
    letter-spacing: 0.6px;
    color: #0f172a;
    text-transform: uppercase;
    margin-bottom: 1px;
  }
  .title {
    font-size: 9.2pt;
    font-weight: 600;
    color: #0284c7;
    margin-bottom: 3px;
    letter-spacing: 0.2px;
  }
  .contact-bar {
    font-size: 8pt;
    color: #475569;
  }
  .contact-bar a {
    color: #0284c7;
    text-decoration: none;
  }
  .separator {
    color: #94a3b8;
    margin: 0 4px;
  }

  /* Section Styling */
  .section {
    margin-bottom: 6px;
  }
  .section-title {
    font-size: 8.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #0f172a;
    border-bottom: 1.2px solid #cbd5e1;
    padding-bottom: 1px;
    margin-bottom: 3px;
  }

  /* Summary */
  .summary-text {
    font-size: 8pt;
    color: #334155;
    line-height: 1.28;
    text-align: justify;
  }

  /* Skills Matrix */
  .skills-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.9pt;
  }
  .skills-table td {
    padding: 1px 0;
    vertical-align: top;
  }
  .skill-category {
    font-weight: 700;
    color: #0f172a;
    width: 21%;
    white-space: nowrap;
  }
  .skill-items {
    color: #334155;
    width: 79%;
  }

  /* Experience & Projects */
  .entry {
    margin-bottom: 4px;
  }
  .entry-header {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 0px;
  }
  .entry-title {
    font-weight: 700;
    font-size: 8.3pt;
    color: #0f172a;
    text-align: left;
  }
  .entry-subtitle {
    font-weight: 600;
    font-size: 8pt;
    color: #0284c7;
  }
  .entry-date {
    font-size: 7.8pt;
    color: #64748b;
    text-align: right;
    font-weight: 500;
    white-space: nowrap;
  }
  .entry-meta {
    font-size: 7.6pt;
    color: #475569;
    font-style: italic;
    margin-bottom: 1.5px;
  }

  /* Bullet Table */
  .bullet-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1px;
  }
  .bullet-table td {
    vertical-align: top;
    padding: 0.8px 0;
    font-size: 7.9pt;
    line-height: 1.24;
    color: #334155;
  }
  .bullet-dot {
    width: 12px;
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
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div class="name">NASIR HAYAT</div>
    <div class="title">DevOps &amp; DevSecOps Engineer &bull; Cloud-Native &amp; Automation</div>
    <div class="contact-bar">
      Peshawar, Pakistan
      <span class="separator">|</span>
      +92 333 9495197
      <span class="separator">|</span>
      <a href="mailto:nasirhayat.dev@gmail.com">nasirhayat.dev@gmail.com</a>
      <span class="separator">|</span>
      <a href="https://www.linkedin.com/in/nasir-hayat-4515202a2">linkedin.com/in/nasir-hayat-4515202a2</a>
      <span class="separator">|</span>
      <a href="https://github.com/nasirhayat028">github.com/nasirhayat028</a>
      <span class="separator">|</span>
      <a href="https://nasirhayat.me">nasirhayat.me</a>
    </div>
  </div>

  <!-- PROFESSIONAL SUMMARY -->
  <div class="section">
    <div class="section-title">Professional Summary</div>
    <div class="summary-text">
      Hands-on DevOps &amp; DevSecOps Engineer with demonstrated expertise in containerization, Kubernetes orchestration, automated CI/CD pipelines, and declarative GitOps delivery. Specializes in shift-left application security (secret scanning, SAST, container vulnerability triage, and DAST), infrastructure reliability, and Linux systems. Passionate about building reproducible, observable delivery workflows and bridging software engineering with secure cloud-native infrastructure.
    </div>
  </div>

  <!-- TECHNICAL SKILLS -->
  <div class="section">
    <div class="section-title">Technical Skills</div>
    <table class="skills-table">
      <tr>
        <td class="skill-category">Cloud &amp; Infrastructure:</td>
        <td class="skill-items">Linux (Bash CLI, Process/Network Inspection, Systemd), AWS (EC2, S3, IAM, CloudWatch, VPC, Security Groups)</td>
      </tr>
      <tr>
        <td class="skill-category">Containers &amp; K8s:</td>
        <td class="skill-items">Docker (Multi-stage builds, Compose, Networks), Kubernetes (kind, Namespaces, Pods, Deployments, Services, ConfigMaps, Secrets, NGINX Ingress)</td>
      </tr>
      <tr>
        <td class="skill-category">CI/CD &amp; GitOps:</td>
        <td class="skill-items">GitHub Actions, Argo CD (Declarative GitOps, Desired State Sync), Jenkins, Git, Docker Hub</td>
      </tr>
      <tr>
        <td class="skill-category">DevSecOps &amp; Security:</td>
        <td class="skill-items">Gitleaks (Secret Scanning), npm audit, SonarQube (SAST), Trivy (Container CVEs), OWASP ZAP (DAST), CSP &amp; HTTP Security Headers</td>
      </tr>
      <tr>
        <td class="skill-category">Observability &amp; Tools:</td>
        <td class="skill-items">Prometheus, Grafana, Vitest, Node.js, Python, Kotlin, React, MongoDB</td>
      </tr>
    </table>
  </div>

  <!-- FEATURED PROJECTS -->
  <div class="section">
    <div class="section-title">Featured Engineering Projects</div>

    <!-- Flagship Project -->
    <div class="entry">
      <table class="entry-header">
        <tr>
          <td class="entry-title">End-to-End DevSecOps Delivery Pipeline &amp; Kubernetes GitOps Platform</td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">GitHub Actions, Docker, Kubernetes (kind), Argo CD, NGINX Ingress, Trivy, SonarQube, Gitleaks, OWASP ZAP</div>
      <table class="bullet-table">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Automated CI/CD Delivery:</b> Engineered full GitHub Actions pipeline running <code>npm ci</code>, Vitest frontend tests, and Node.js backend integration tests, building version-tagged Docker images (<code>build-&lt;num&gt;</code>) pushed to Docker Hub.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Shift-Left Security Architecture:</b> Integrated a 4-tier security barrier into CI: <b>Gitleaks</b> (credential detection), <b>npm audit</b> (high-severity dependency gating), <b>SonarQube</b> (static analysis &amp; code quality), and <b>Trivy</b> (container vulnerability triage).</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>GitOps Reconciliation:</b> Deployed <b>Argo CD</b> on a local multi-node <b>kind</b> cluster (<code>dev-cluster</code>, namespace <code>noteapp</code>) to automate continuous desired-state synchronization and cluster health monitoring.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Cloud-Native Ingress &amp; Routing:</b> Configured <b>NGINX Ingress Controller</b> to route external traffic (<code>notes.local</code>) to frontend and backend ClusterIP services with internal MongoDB isolation.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>DAST &amp; Response Hardening:</b> Executed containerized <b>OWASP ZAP</b> baseline scans; remediated missing Content-Security-Policy alerts by configuring enforcing CSP, X-Frame-Options, X-Content-Type-Options, and Referrer-Policy on NGINX.</td>
        </tr>
      </table>
    </div>

    <!-- TeamSyncAI Project -->
    <div class="entry">
      <table class="entry-header">
        <tr>
          <td class="entry-title">TeamSyncAI &ndash; Android Collaboration &amp; Organizational Workspace Platform</td>
          <td class="entry-date">2025 &ndash; 2026</td>
        </tr>
      </table>
      <div class="entry-meta">Kotlin, Jetpack Compose, Hilt DI, Firebase Auth/Firestore/Storage, Unit Testing, ProGuard/R8</div>
      <table class="bullet-table">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Architecture &amp; RBAC:</b> Designed scalable collaborative platform with multi-tenant workspace isolation and role-based access control (Owner, Admin, Manager, Employee), featuring attendance tracking, real-time chat, and announcements.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Reliability &amp; Build Hardening:</b> Maintained high software quality with <b>19/19 passing automated unit tests</b>, strict MVVM/Repository separation, and verified release/R8 obfuscation builds.</td>
        </tr>
      </table>
    </div>

    <!-- AI MCQ Project -->
    <div class="entry">
      <table class="entry-header">
        <tr>
          <td class="entry-title">Multi-Model AI Consensus Engine &ndash; Browser Extension</td>
          <td class="entry-date">2026</td>
        </tr>
      </table>
      <div class="entry-meta">Chrome Manifest V3, TypeScript, React, OpenAI API, Anthropic Claude API, Google Gemini API</div>
      <table class="bullet-table">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Multi-LLM Orchestration:</b> Architected Chrome extension comparing responses across OpenAI, Gemini, and Claude models to surface agreement, variance, and uncertainty signals rather than trusting single-model output.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text"><b>Security &amp; Extensibility:</b> Built clean provider abstraction layers with schema validation and secure client-side API key isolation adhering to Manifest V3 security requirements.</td>
        </tr>
      </table>
    </div>
  </div>

  <!-- WORK EXPERIENCE -->
  <div class="section">
    <div class="section-title">Work Experience</div>
    <div class="entry">
      <table class="entry-header">
        <tr>
          <td class="entry-title">CodeOps Pro <span class="entry-subtitle">&ndash; DevOps Engineering Intern</span></td>
          <td class="entry-date">May 2025 &ndash; Jul 2025 (Remote)</td>
        </tr>
      </table>
      <table class="bullet-table">
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Containerized multi-tier applications using <b>Docker</b> and multi-stage builds, standardizing development and deployment environments.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Configured <b>Kubernetes</b> workloads (Deployments, ClusterIP/NodePort Services, ConfigMaps, and Secrets) for isolated application delivery.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Deployed <b>Prometheus &amp; Grafana</b> monitoring stacks to visualize node resources, container metrics, and application performance.</td>
        </tr>
        <tr>
          <td class="bullet-dot">&bull;</td>
          <td class="bullet-text">Troubleshot Linux system processes, file permissions, and container networking to ensure reproducible release cycles.</td>
        </tr>
      </table>
    </div>
  </div>

  <!-- EDUCATION & CERTIFICATIONS (2 COLUMNS) -->
  <div class="section">
    <table class="two-col">
      <tr>
        <td class="col-left">
          <div class="section-title">Education</div>
          <div class="entry">
            <div class="entry-title">Kohat University of Science &amp; Technology (KUST)</div>
            <div class="entry-subtitle" style="color: #334155; font-weight: 500;">BS in Computer Science &bull; 7th Semester</div>
            <div class="entry-date" style="text-align: left; margin-top: 1px;">2023 &ndash; 2027 (In Progress)</div>
          </div>
        </td>
        <td class="col-right">
          <div class="section-title">Certifications &amp; Training</div>
          <div class="entry">
            <table class="bullet-table">
              <tr>
                <td class="bullet-dot">&bull;</td>
                <td class="bullet-text"><b>Certified Kubernetes Administrator (CKA Track)</b> &ndash; KodeKloud</td>
              </tr>
              <tr>
                <td class="bullet-dot">&bull;</td>
                <td class="bullet-text"><b>AWS DevOps Engineering Program</b> &ndash; Honhar Tech Initiative</td>
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
    
    html = generate_resume_html()
    
    # Save HTML file
    html_path = "/home/nasir/Desktop/CV/Nasir_Hayat_DevOps_Resume.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved HTML to {html_path}")

    # Write PDF
    pdf_path = "/home/nasir/Desktop/CV/Nasir_Hayat_DevOps_Resume.pdf"
    doc = QTextDocument()
    doc.setHtml(html)
    
    writer = QPdfWriter(pdf_path)
    writer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
    
    # Margins: 6mm top/bottom, 8mm left/right
    layout = QPageLayout(
        QPageSize(QPageSize.PageSizeId.A4),
        QPageLayout.Orientation.Portrait,
        QMarginsF(8, 6, 8, 6),
        QPageLayout.Unit.Millimeter
    )
    writer.setPageLayout(layout)
    
    paint_size = layout.paintRectPoints()
    doc.setPageSize(QSizeF(paint_size.width(), paint_size.height()))
    print("Pre-print doc pageCount:", doc.pageCount())
    doc.print_(writer)
    print(f"Saved PDF to {pdf_path}")

if __name__ == "__main__":
    build_pdf()
