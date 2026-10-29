#!/usr/bin/env python3
"""
build_cv.py
Generates Nasir Hayat's single-page CV matching the exact visual design,
Carlito/Calibri font styling, bold/regular distribution, borders, and structure
of Kafayat_Ullah_Afridi_CV.pdf.

Outputs:
  - Nasir_Hayat_CV.docx (editable Word document with Carlito/Calibri styling)
  - Nasir_Hayat_CV.html (clean HTML template embedding local Carlito font)
  - Nasir_Hayat_CV.pdf  (strict single-page PDF via headless Chrome)
"""

import os
import subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "fonts")

def create_docx(docx_path):
    doc = docx.Document()
    
    # Page setup: A4 with 0.38 inch (9.6mm) top/bottom, 0.48 inch (12.2mm) left/right margins
    section = doc.sections[0]
    section.page_width = Inches(8.27)   # 210 mm
    section.page_height = Inches(11.69) # 297 mm
    section.top_margin = Inches(0.38)
    section.bottom_margin = Inches(0.38)
    section.left_margin = Inches(0.48)
    section.right_margin = Inches(0.48)
    
    # Configure Normal style: Carlito / Calibri font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Carlito'
    font.size = Pt(9.0)
    font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    
    def format_p(p, space_before=0, space_after=0, line_spacing=1.11, align=WD_ALIGN_PARAGRAPH.LEFT):
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        p.alignment = align

    def apply_font(run, bold=False, size=Pt(9.0), color=RGBColor(0, 0, 0)):
        run.bold = bold
        run.font.name = 'Carlito'
        run.font.size = size
        run.font.color.rgb = color
        # Set rFonts for Word compatibility
        rPr = run._r.get_or_add_rPr()
        rFonts = parse_xml(r'<w:rFonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
                           r'w:ascii="Carlito" w:hAnsi="Carlito" w:cs="Carlito"/>')
        rPr.append(rFonts)

    def add_section_heading(title, space_before=5.0, space_after=1.8):
        p = doc.add_paragraph()
        format_p(p, space_before=space_before, space_after=space_after, line_spacing=1.0)
        run = p.add_run(title)
        apply_font(run, bold=True, size=Pt(10.2))
        
        # Add thin black bottom border matching reference
        pPr = p._p.get_or_add_pPr()
        pBdr = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                         r'<w:bottom w:val="single" w:sz="6" w:space="1" w:color="000000"/>'
                         r'</w:pBdr>')
        pPr.append(pBdr)
        return p

    def add_hyperlink(paragraph, url, text, color="0563C1", underline=True, font_size=Pt(9.0)):
        part = paragraph.part
        r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
        sz_val = int(font_size.pt * 2)
        u_tag = '<w:u w:val="single"/>' if underline else ''
        hyperlink_xml = (
            f'<w:hyperlink xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            f'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="{r_id}">'
            f'<w:r>'
            f'<w:rPr>'
            f'<w:rFonts w:ascii="Carlito" w:hAnsi="Carlito" w:cs="Carlito"/>'
            f'<w:color w:val="{color}"/>'
            f'{u_tag}'
            f'<w:sz w:val="{sz_val}"/>'
            f'</w:rPr>'
            f'<w:t xml:space="preserve">{text}</w:t>'
            f'</w:r>'
            f'</w:hyperlink>'
        )
        paragraph._p.append(parse_xml(hyperlink_xml))

    def add_bullet(text_runs, space_after=1.0):
        p = doc.add_paragraph()
        format_p(p, space_before=0, space_after=space_after, line_spacing=1.11)
        p.paragraph_format.left_indent = Inches(0.18)
        p.paragraph_format.first_line_indent = Inches(-0.13)
        
        r_bullet = p.add_run("• ")
        apply_font(r_bullet, bold=False, size=Pt(9.0))
        
        for text, bold in text_runs:
            r = p.add_run(text)
            apply_font(r, bold=bold, size=Pt(9.0))
        return p

    # 1. HEADER
    # Name: BOLD 19.5pt
    p_name = doc.add_paragraph()
    format_p(p_name, space_before=0, space_after=0.8, line_spacing=1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_name = p_name.add_run("Nasir Hayat")
    apply_font(r_name, bold=True, size=Pt(19.5))

    # Job Title: BOLD 10.2pt
    p_title = doc.add_paragraph()
    format_p(p_title, space_before=0, space_after=1.6, line_spacing=1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_title = p_title.add_run("Junior DevOps & DevSecOps Engineer")
    apply_font(r_title, bold=True, size=Pt(10.2))

    # Contact line 1: Location, Phone, Email
    p_c1 = doc.add_paragraph()
    format_p(p_c1, space_before=0, space_after=0.8, line_spacing=1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_loc = p_c1.add_run("Peshawar, Pakistan | +92 333 9495197 | ")
    apply_font(r_loc, bold=False, size=Pt(9.0))
    add_hyperlink(p_c1, "mailto:nasirhayat.dev@gmail.com", "nasirhayat.dev@gmail.com")

    # Contact line 2: GitHub full URL, LinkedIn full URL
    p_c2 = doc.add_paragraph()
    format_p(p_c2, space_before=0, space_after=2.0, line_spacing=1.0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_gh_l = p_c2.add_run("GitHub: ")
    apply_font(r_gh_l, bold=False, size=Pt(9.0))
    add_hyperlink(p_c2, "https://github.com/nasirhayat028", "github.com/nasirhayat028")
    r_sep = p_c2.add_run(" | ")
    apply_font(r_sep, bold=False, size=Pt(9.0))
    r_li_l = p_c2.add_run("LinkedIn: ")
    apply_font(r_li_l, bold=False, size=Pt(9.0))
    add_hyperlink(p_c2, "https://www.linkedin.com/in/nasir-hayat-4515202a2", "linkedin.com/in/nasir-hayat-4515202a2")

    # 2. PROFESSIONAL SUMMARY
    add_section_heading("PROFESSIONAL SUMMARY", space_before=4.2, space_after=1.6)
    p_sum = doc.add_paragraph()
    format_p(p_sum, space_before=0.5, space_after=1.8, line_spacing=1.11)
    r_sum = p_sum.add_run(
        "Junior DevOps & DevSecOps Engineer skilled in automating CI/CD pipelines, securing cloud-native infrastructure, "
        "and managing Kubernetes workloads. Hands-on experience integrating shift-left security practices, including "
        "SAST, secrets detection, container vulnerability scanning, and DAST, alongside declarative GitOps with Argo CD. "
        "Hands-on practice with Linux, AWS cloud services, and secure containerized deployments."
    )
    apply_font(r_sum, bold=False, size=Pt(9.0))

    # 3. EDUCATION
    add_section_heading("EDUCATION", space_before=4.5, space_after=1.6)
    
    # Entry 1: BS CS
    p_edu1 = doc.add_paragraph()
    format_p(p_edu1, space_before=0.5, space_after=0.3, line_spacing=1.11)
    r_edu1_b = p_edu1.add_run("Bachelor of Science in Computer Science")
    apply_font(r_edu1_b, bold=True, size=Pt(9.0))
    r_edu1_r = p_edu1.add_run(", Kohat University of Science and Technology (KUST), Kohat, Pakistan")
    apply_font(r_edu1_r, bold=False, size=Pt(9.0))

    p_edu1_sub = doc.add_paragraph()
    format_p(p_edu1_sub, space_before=0, space_after=1.2, line_spacing=1.11)
    r_edu1_sub = p_edu1_sub.add_run("2023 – Expected 2027")
    apply_font(r_edu1_sub, bold=False, size=Pt(9.0))

    # Entry 2: DIT
    p_edu2 = doc.add_paragraph()
    format_p(p_edu2, space_before=0.4, space_after=0.3, line_spacing=1.11)
    r_edu2_b = p_edu2.add_run("Diploma in Information Technology (DIT)")
    apply_font(r_edu2_b, bold=True, size=Pt(9.0))
    r_edu2_r = p_edu2.add_run(", Islamic Institute of English Language & Computer, Hangu, Pakistan")
    apply_font(r_edu2_r, bold=False, size=Pt(9.0))

    p_edu2_sub = doc.add_paragraph()
    format_p(p_edu2_sub, space_before=0, space_after=1.8, line_spacing=1.11)
    r_edu2_sub = p_edu2_sub.add_run("2022")
    apply_font(r_edu2_sub, bold=False, size=Pt(9.0))

    # 4. TECHNICAL SKILLS
    add_section_heading("TECHNICAL SKILLS", space_before=4.5, space_after=1.6)
    skills = [
        ("Cloud (AWS): ", "EKS, EC2, ECR, VPC, Subnets, Route Tables, NAT Gateway, Security Groups, Application Load Balancer (ALB), IAM, S3, CloudWatch"),
        ("Containers: ", "Docker (multi-stage builds), Container Registries (Amazon ECR, Docker Hub)"),
        ("Kubernetes: ", "Deployments, Services, Namespaces, ConfigMaps, Secrets, Ingress, AWS Load Balancer Controller, Persistent Volumes & PVCs, EBS CSI Driver, Health Probes, Resource Limits, HPA"),
        ("Kubernetes Security & Governance: ", "RBAC, Service Accounts, NetworkPolicies, ResourceQuotas, LimitRanges, PodDisruptionBudgets"),
        ("CI/CD & GitOps: ", "Git, GitHub Actions, Jenkins, Groovy Shared Libraries, Argo CD"),
        ("DevSecOps: ", "Gitleaks (secrets detection), npm audit (SCA), SonarQube (SAST), Trivy (container vulnerability scanning), OWASP ZAP (DAST), Container Hardening (non-root, multi-stage)"),
        ("Monitoring: ", "Prometheus (metrics, alerting), Grafana (dashboards)"),
        ("Databases: ", "MongoDB, PostgreSQL, Redis"),
        ("Linux & Scripting: ", "Linux, Bash, Systemd, Networking")
    ]
    for cat, items in skills:
        p_sk = doc.add_paragraph()
        format_p(p_sk, space_before=0, space_after=0.9, line_spacing=1.11)
        r_cat = p_sk.add_run(cat)
        apply_font(r_cat, bold=True, size=Pt(9.0))
        r_it = p_sk.add_run(items)
        apply_font(r_it, bold=False, size=Pt(9.0))

    # 5. EXPERIENCE
    add_section_heading("EXPERIENCE", space_before=4.5, space_after=1.6)
    
    # Role 1: CodeOps Pro
    p_exp1 = doc.add_paragraph()
    format_p(p_exp1, space_before=0.5, space_after=0.3, line_spacing=1.11)
    r_e1_b = p_exp1.add_run("DevOps Engineering Intern")
    apply_font(r_e1_b, bold=True, size=Pt(9.0))
    r_e1_r = p_exp1.add_run(", CodeOps Pro")
    apply_font(r_e1_r, bold=False, size=Pt(9.0))

    p_exp1_sub = doc.add_paragraph()
    format_p(p_exp1_sub, space_before=0, space_after=0.8, line_spacing=1.11)
    r_e1_sub = p_exp1_sub.add_run("Jul 2025 – Sep 2025 (3 months) | Remote")
    apply_font(r_e1_sub, bold=False, size=Pt(9.0))

    add_bullet([("Containerized microservices using Docker multi-stage builds to standardize development and runtime environments.", False)])
    add_bullet([("Configured Kubernetes workloads, including Deployments, Services, ConfigMaps, and Secrets, with health probes and resource limits.", False)])
    add_bullet([("Deployed Prometheus and Grafana to monitor container metrics and cluster health.", False)])
    add_bullet([("Automated CI/CD workflows for version-tagged Docker image builds and Docker Hub publishing.", False)], space_after=1.6)

    # 6. TRAINING
    add_section_heading("TRAINING", space_before=4.5, space_after=1.6)
    p_tr = doc.add_paragraph()
    format_p(p_tr, space_before=0.5, space_after=0.8, line_spacing=1.11)
    r_tr_b = p_tr.add_run("AWS re/Start Graduate")
    apply_font(r_tr_b, bold=True, size=Pt(9.0))
    r_tr_m = p_tr.add_run(" | LearnTechGlobal (AWS re/Start program) | Aug 2026 – Present")
    apply_font(r_tr_m, bold=False, size=Pt(9.0))

    add_bullet([("Completing an intensive cloud skills program covering Linux, networking, security fundamentals, and core AWS services (EC2, VPC, S3, IAM, CloudWatch).", False)])
    add_bullet([("Performing hands-on labs in live AWS environments via the Canvas learning platform, including launching and configuring an EC2 web server with User Data (Apache) and Security Groups, monitoring it with EC2 status checks and CloudWatch metrics, resizing instance and EBS volume, enabling and disabling Termination Protection, and building a VPC with public and private subnets, an Internet Gateway, and route tables, troubleshooting SSH connectivity through the route table.", False)], space_after=1.6)

    # 7. PROJECTS
    add_section_heading("PROJECTS", space_before=4.5, space_after=1.6)

    # Project 1: AWS EKS
    p_peks = doc.add_paragraph()
    format_p(p_peks, space_before=0.5, space_after=0.8, line_spacing=1.11)
    r_peks_t = p_peks.add_run("AWS EKS Infrastructure & Application Deployment")
    apply_font(r_peks_t, bold=True, size=Pt(9.0))
    r_peks_s = p_peks.add_run(" | ")
    apply_font(r_peks_s, bold=False, size=Pt(9.0))
    add_hyperlink(p_peks, "https://github.com/nasirhayat028/notes-app-aws-eks-deployment", "GitHub")

    add_bullet([("Provisioned an Amazon EKS cluster inside a custom VPC configured with subnets, route tables, and a NAT Gateway", False)])
    add_bullet([("Containerized frontend and backend services using Docker and pushed application images to Amazon ECR", False)])
    add_bullet([("Deployed frontend, backend, and MongoDB workloads using Kubernetes Deployments and Services with PersistentVolumeClaims backed by Amazon EBS via the EBS CSI Driver", False)])
    add_bullet([("Exposed the application publicly using AWS Load Balancer Controller, Ingress, and an Application Load Balancer (ALB), while configuring IAM permissions for cluster add-ons", False)])
    add_bullet([("Verified public access, user registration and login workflows, and database CRUD functionality end to end", False)], space_after=1.5)

    # Project 2: DevSecOps Pipeline
    p_p1 = doc.add_paragraph()
    format_p(p_p1, space_before=0.6, space_after=0.8, line_spacing=1.11)
    r_p1_t = p_p1.add_run("End-to-End DevSecOps Pipeline & GitOps Platform")
    apply_font(r_p1_t, bold=True, size=Pt(9.0))
    r_p1_s = p_p1.add_run(" | ")
    apply_font(r_p1_s, bold=False, size=Pt(9.0))
    add_hyperlink(p_p1, "https://github.com/nasirhayat028/notes-webapp", "GitHub")

    add_bullet([("Automated GitHub Actions CI pipeline running multi-stage security scans: Gitleaks, npm audit, SonarQube, and Trivy", False)])
    add_bullet([("Configured Argo CD for declarative GitOps continuous delivery and application health checks on Kubernetes", False)])
    add_bullet([("Configured NGINX Ingress for traffic routing and integrated containerized OWASP ZAP baseline DAST scans", False)])
    add_bullet([("Automated container builds with build-number-tagged Docker images published to Docker Hub and updated GitOps repo", False)], space_after=1.5)

    # Project 3: Kubernetes Security & Governance
    p_p2 = doc.add_paragraph()
    format_p(p_p2, space_before=0.6, space_after=0.8, line_spacing=1.11)
    r_p2_t = p_p2.add_run("Kubernetes Security & Workload Governance")
    apply_font(r_p2_t, bold=True, size=Pt(9.0))
    r_p2_s = p_p2.add_run(" | ")
    apply_font(r_p2_s, bold=False, size=Pt(9.0))
    add_hyperlink(p_p2, "https://github.com/nasirhayat028/devtrack-pms-DevSecOps", "GitHub")

    add_bullet([("Authored Kubernetes NetworkPolicies restricting database ingress exclusively to authorized backend pods", False)])
    add_bullet([("Implemented LimitRanges, ResourceQuotas, and backend PodDisruptionBudgets (PDB) for workload governance", False)])
    add_bullet([("Built multi-stage Dockerfiles enforcing non-root user execution with rolling update settings for backend", False)], space_after=1.5)

    # Project 4: Jenkins Shared Libraries
    p_p3 = doc.add_paragraph()
    format_p(p_p3, space_before=0.6, space_after=0.8, line_spacing=1.11)
    r_p3_t = p_p3.add_run("Jenkins Shared Libraries & CI/CD Automation")
    apply_font(r_p3_t, bold=True, size=Pt(9.0))
    r_p3_s = p_p3.add_run(" | ")
    apply_font(r_p3_s, bold=False, size=Pt(9.0))
    add_hyperlink(p_p3, "https://github.com/nasirhayat028/jenkins-shared-libraries-01", "GitHub")

    add_bullet([("Developed modular Jenkins shared library functions (vars/) standardizing source checkout and Docker builds", False)])
    add_bullet([("Configured parameter-driven build steps supporting custom Dockerfile paths, build contexts, and image tags", False)])
    add_bullet([("Automated secure container image publishing to Docker registry utilizing Jenkins credentials binding", False)], space_after=0)

    doc.save(docx_path)
    print(f"Successfully generated DOCX: {docx_path}")

def generate_html(html_path):
    carlito_regular_path = os.path.join(FONTS_DIR, "Carlito-Regular.ttf")
    carlito_bold_path = os.path.join(FONTS_DIR, "Carlito-Bold.ttf")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Nasir Hayat - Junior DevOps &amp; DevSecOps Engineer CV</title>
<style>
  @font-face {{
    font-family: 'Carlito';
    src: url('{carlito_regular_path}') format('truetype');
    font-weight: normal;
    font-style: normal;
  }}
  @font-face {{
    font-family: 'Carlito';
    src: url('{carlito_bold_path}') format('truetype');
    font-weight: bold;
    font-style: normal;
  }}

  @page {{
    size: A4 portrait;
    margin: 8.5mm 12.0mm 8.5mm 12.0mm;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    font-family: 'Carlito', Calibri, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #000000;
    font-size: 9.0pt;
    line-height: 1.15;
    background: #ffffff;
    -webkit-font-smoothing: antialiased;
  }}

  /* Header */
  .header {{
    text-align: center;
    margin-bottom: 3.0px;
  }}
  .name {{
    font-size: 19.5pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 0.8px;
    letter-spacing: 0.1px;
  }}
  .title {{
    font-size: 10.2pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 1.2px;
  }}
  .contact-line {{
    font-size: 9.0pt;
    font-weight: normal;
    color: #000000;
    line-height: 1.2;
  }}
  .contact-line a {{
    color: #0563C1;
    text-decoration: underline;
  }}
  .sep {{
    color: #000000;
    margin: 0 4px;
  }}

  /* Section Headings */
  .section-title {{
    font-size: 10.2pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #000000;
    border-bottom: 1.0px solid #000000;
    padding-bottom: 0.8px;
    margin-top: 4.8px;
    margin-bottom: 1.8px;
    letter-spacing: 0.2px;
  }}

  /* Summary */
  .summary-text {{
    font-size: 9.0pt;
    font-weight: normal;
    line-height: 1.15;
    color: #000000;
    text-align: justify;
    margin-bottom: 2.0px;
  }}

  /* Education */
  .edu-block {{
    margin-bottom: 1.6px;
  }}
  .edu-line {{
    font-size: 9.0pt;
    line-height: 1.14;
    color: #000000;
    margin-bottom: 0.3px;
  }}
  .edu-line strong {{
    font-weight: bold;
  }}
  .edu-meta {{
    font-size: 9.0pt;
    font-weight: normal;
    line-height: 1.14;
    color: #000000;
  }}

  /* Technical Skills */
  .skills-list {{
    margin-bottom: 2.2px;
  }}
  .skill-item {{
    font-size: 9.0pt;
    font-weight: normal;
    line-height: 1.15;
    margin-bottom: 1.0px;
    color: #000000;
  }}
  .skill-item strong {{
    font-weight: bold;
  }}

  /* Training */
  .entry-block {{
    margin-bottom: 2.0px;
  }}
  .entry-title {{
    font-size: 9.0pt;
    color: #000000;
    margin-bottom: 0.3px;
  }}
  .entry-title strong {{
    font-weight: bold;
  }}
  .entry-meta {{
    font-size: 9.0pt;
    font-weight: normal;
    color: #000000;
    margin-bottom: 0.8px;
  }}

  /* Projects */
  .project-title {{
    font-size: 9.0pt;
    line-height: 1.15;
    margin-bottom: 0.8px;
    color: #000000;
  }}
  .project-title strong {{
    font-weight: bold;
  }}
  .project-title a {{
    color: #0563C1;
    text-decoration: underline;
    font-weight: normal;
  }}

  /* Bullets */
  .bullet-list {{
    list-style-type: none;
    margin: 0;
    padding: 0;
  }}
  .bullet-list li {{
    position: relative;
    padding-left: 13px;
    font-size: 9.0pt;
    font-weight: normal;
    line-height: 1.15;
    color: #000000;
    margin-bottom: 1.0px;
  }}
  .bullet-list li::before {{
    content: "•";
    position: absolute;
    left: 2px;
    top: 0;
    color: #000000;
    font-size: 9.2pt;
  }}
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div class="name">Nasir Hayat</div>
    <div class="title">Junior DevOps &amp; DevSecOps Engineer</div>
    <div class="contact-line">
      <span>Peshawar, Pakistan</span>
      <span class="sep">|</span>
      <span>+92 333 9495197</span>
      <span class="sep">|</span>
      <a href="mailto:nasirhayat.dev@gmail.com">nasirhayat.dev@gmail.com</a>
    </div>
    <div class="contact-line" style="margin-top: 1.0px;">
      <span>GitHub: <a href="https://github.com/nasirhayat028">github.com/nasirhayat028</a></span>
      <span class="sep">|</span>
      <span>LinkedIn: <a href="https://www.linkedin.com/in/nasir-hayat-4515202a2">linkedin.com/in/nasir-hayat-4515202a2</a></span>
    </div>
  </div>

  <!-- PROFESSIONAL SUMMARY -->
  <div class="section-title">PROFESSIONAL SUMMARY</div>
  <div class="summary-text">
    Junior DevOps &amp; DevSecOps Engineer skilled in automating CI/CD pipelines, securing cloud-native infrastructure, and managing Kubernetes workloads. Hands-on experience integrating shift-left security practices, including SAST, secrets detection, container vulnerability scanning, and DAST, alongside declarative GitOps with Argo CD. Hands-on practice with Linux, AWS cloud services, and secure containerized deployments.
  </div>

  <!-- EDUCATION -->
  <div class="section-title">EDUCATION</div>
  <div class="edu-block">
    <div class="edu-line"><strong>Bachelor of Science in Computer Science</strong>, Kohat University of Science and Technology (KUST), Kohat, Pakistan</div>
    <div class="edu-meta">2023 – Expected 2027</div>
  </div>
  <div class="edu-block" style="margin-bottom: 2.0px;">
    <div class="edu-line"><strong>Diploma in Information Technology (DIT)</strong>, Islamic Institute of English Language &amp; Computer, Hangu, Pakistan</div>
    <div class="edu-meta">2022</div>
  </div>

  <!-- TECHNICAL SKILLS -->
  <div class="section-title">TECHNICAL SKILLS</div>
  <div class="skills-list">
    <div class="skill-item"><strong>Cloud (AWS):</strong> EKS, EC2, ECR, VPC, Subnets, Route Tables, NAT Gateway, Security Groups, Application Load Balancer (ALB), IAM, S3, CloudWatch</div>
    <div class="skill-item"><strong>Containers:</strong> Docker (multi-stage builds), Container Registries (Amazon ECR, Docker Hub)</div>
    <div class="skill-item"><strong>Kubernetes:</strong> Deployments, Services, Namespaces, ConfigMaps, Secrets, Ingress, AWS Load Balancer Controller, Persistent Volumes &amp; PVCs, EBS CSI Driver, Health Probes, Resource Limits, HPA</div>
    <div class="skill-item"><strong>Kubernetes Security &amp; Governance:</strong> RBAC, Service Accounts, NetworkPolicies, ResourceQuotas, LimitRanges, PodDisruptionBudgets</div>
    <div class="skill-item"><strong>CI/CD &amp; GitOps:</strong> Git, GitHub Actions, Jenkins, Groovy Shared Libraries, Argo CD</div>
    <div class="skill-item"><strong>DevSecOps:</strong> Gitleaks (secrets detection), npm audit (SCA), SonarQube (SAST), Trivy (container vulnerability scanning), OWASP ZAP (DAST), Container Hardening (non-root, multi-stage)</div>
    <div class="skill-item"><strong>Monitoring:</strong> Prometheus (metrics, alerting), Grafana (dashboards)</div>
    <div class="skill-item"><strong>Databases:</strong> MongoDB, PostgreSQL, Redis</div>
    <div class="skill-item"><strong>Linux &amp; Scripting:</strong> Linux, Bash, Systemd, Networking</div>
  </div>

  <!-- EXPERIENCE -->
  <div class="section-title">EXPERIENCE</div>
  
  <div class="entry-block">
    <div class="entry-title"><strong>DevOps Engineering Intern</strong>, CodeOps Pro</div>
    <div class="entry-meta">Jul 2025 – Sep 2025 (3 months) | Remote</div>
    <ul class="bullet-list">
      <li>Containerized microservices using Docker multi-stage builds to standardize development and runtime environments.</li>
      <li>Configured Kubernetes workloads, including Deployments, Services, ConfigMaps, and Secrets, with health probes and resource limits.</li>
      <li>Deployed Prometheus and Grafana to monitor container metrics and cluster health.</li>
      <li>Automated CI/CD workflows for version-tagged Docker image builds and Docker Hub publishing.</li>
    </ul>
  </div>

  <!-- TRAINING -->
  <div class="section-title">TRAINING</div>
  <div class="entry-block">
    <div class="entry-title"><strong>AWS re/Start Graduate</strong> | LearnTechGlobal (AWS re/Start program) | Aug 2026 – Present</div>
    <ul class="bullet-list">
      <li>Completing an intensive cloud skills program covering Linux, networking, security fundamentals, and core AWS services (EC2, VPC, S3, IAM, CloudWatch).</li>
      <li>Performing hands-on labs in live AWS environments via the Canvas learning platform, including launching and configuring an EC2 web server with User Data (Apache) and Security Groups, monitoring it with EC2 status checks and CloudWatch metrics, resizing instance and EBS volume, enabling and disabling Termination Protection, and building a VPC with public and private subnets, an Internet Gateway, and route tables, troubleshooting SSH connectivity through the route table.</li>
    </ul>
  </div>

  <!-- PROJECTS -->
  <div class="section-title">PROJECTS</div>

  <div class="entry-block">
    <div class="project-title"><strong>AWS EKS Infrastructure &amp; Application Deployment</strong> | <a href="https://github.com/nasirhayat028/notes-app-aws-eks-deployment">GitHub</a></div>
    <ul class="bullet-list">
      <li>Provisioned an Amazon EKS cluster inside a custom VPC configured with subnets, route tables, and a NAT Gateway</li>
      <li>Containerized frontend and backend services using Docker and pushed application images to Amazon ECR</li>
      <li>Deployed frontend, backend, and MongoDB workloads using Kubernetes Deployments and Services with PersistentVolumeClaims backed by Amazon EBS via the EBS CSI Driver</li>
      <li>Exposed the application publicly using AWS Load Balancer Controller, Ingress, and an Application Load Balancer (ALB), while configuring IAM permissions for cluster add-ons</li>
      <li>Verified public access, user registration and login workflows, and database CRUD functionality end to end</li>
    </ul>
  </div>

  <div class="entry-block" style="margin-top: 1.8px;">
    <div class="project-title"><strong>End-to-End DevSecOps Pipeline &amp; GitOps Platform</strong> | <a href="https://github.com/nasirhayat028/notes-webapp">GitHub</a></div>
    <ul class="bullet-list">
      <li>Automated GitHub Actions CI pipeline running multi-stage security scans: Gitleaks, npm audit, SonarQube, and Trivy</li>
      <li>Configured Argo CD for declarative GitOps continuous delivery and application health checks on Kubernetes</li>
      <li>Configured NGINX Ingress for traffic routing and integrated containerized OWASP ZAP baseline DAST scans</li>
      <li>Automated container builds with build-number-tagged Docker images published to Docker Hub and updated GitOps repo</li>
    </ul>
  </div>

  <div class="entry-block" style="margin-top: 1.8px;">
    <div class="project-title"><strong>Kubernetes Security &amp; Workload Governance</strong> | <a href="https://github.com/nasirhayat028/devtrack-pms-DevSecOps">GitHub</a></div>
    <ul class="bullet-list">
      <li>Authored Kubernetes NetworkPolicies restricting database ingress exclusively to authorized backend pods</li>
      <li>Implemented LimitRanges, ResourceQuotas, and backend PodDisruptionBudgets (PDB) for workload governance</li>
      <li>Built multi-stage Dockerfiles enforcing non-root user execution with rolling update settings for backend</li>
    </ul>
  </div>

  <div class="entry-block" style="margin-top: 1.8px;">
    <div class="project-title"><strong>Jenkins Shared Libraries &amp; CI/CD Automation</strong> | <a href="https://github.com/nasirhayat028/jenkins-shared-libraries-01">GitHub</a></div>
    <ul class="bullet-list">
      <li>Developed modular Jenkins shared library functions (vars/) standardizing source checkout and Docker builds</li>
      <li>Configured parameter-driven build steps supporting custom Dockerfile paths, build contexts, and image tags</li>
      <li>Automated secure container image publishing to Docker registry utilizing Jenkins credentials binding</li>
    </ul>
  </div>

</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated HTML: {html_path}")

def export_pdf_chrome(html_path, pdf_path):
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--allow-file-access-from-files",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print(f"Successfully exported PDF via Chrome: {pdf_path}")

def check_pdf_pages(pdf_path):
    try:
        res = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True, check=True)
        for line in res.stdout.splitlines():
            if "Pages:" in line:
                print("PDF Info:", line.strip())
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return None

if __name__ == "__main__":
    workdir = BASE_DIR
    docx_file = os.path.join(workdir, "Nasir_Hayat_CV.docx")
    html_file = os.path.join(workdir, "Nasir_Hayat_CV.html")
    pdf_file = os.path.join(workdir, "Nasir_Hayat_CV.pdf")
    
    create_docx(docx_file)
    generate_html(html_file)
    export_pdf_chrome(html_file, pdf_file)
    pages = check_pdf_pages(pdf_file)
    print(f"Verification complete. Total pages: {pages}")
