from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Portfolio API", version="1.0.0")

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static content payload
CONTENT = {
  "header": {
    "title": "Taahier Mahammad",
    "tagline": "Innovate. Build. Secure.",
    "description": "Transform your ideas into bulletproof digital solutions. I craft secure, lightning-fast applications that don't just work—they dominate.",
    "sections": ["Intro", "Education", "Skills", "Projects", "Contact"]
  },
  "about": {
    "name": "Taahier Mhd",
    "intro_image": "images/intro_image.jpg",
    "summary": [
      "I'm a passionate Software Developer, Backend Engineer, and Cybersecurity Specialist who thrives on turning complex challenges into elegant solutions.",
      "My journey spans from crafting robust backend systems to implementing cutting-edge security measures."
    ],
    "expertise": {
      "application_development": "Building robust system architectures leveraging Java, MySQL, J2EE, and OOP.",
      "web_development": "Responsive, high-performance websites and web apps.",
      "cloud": "AWS and Azure solutions with reliability and scalability.",
      "cybersecurity": "Security-focused development with modern defense practices."
    }
  },
  "what_i_offer": [
    {"title": "Streamlined Work Processes", "description": "Efficient workflows and automation tools for improved performance."},
    {"title": "Integrated Security Measures", "description": "Comprehensive measures to safeguard systems and data."},
    {"title": "Tailored Support & Maintenance", "description": "Complete support and maintenance for seamless functioning."},
    {"title": "Innovative Solutions for the Future", "description": "Implementation of forward-thinking technologies."}
  ],
  "ready_for_team": [
    "Application & Backend Development",
    "Cloud Engineering",
    "Cybersecurity"
  ],
  "education": {
    "degree": [
      {"title": "B.Tech", "institute": "Sri Venkateswara Engineering College, Tirupathi", "branch": "Electrical and Electronics Engineering"},
      {"title": "Diploma", "institute": "Government Polytechnic College, Ananthapur", "branch": "Electrical and Electronics Engineering"},
      {"title": "SSC", "institute": "Mourya High School, Tadipatri"}
    ],
    "certifications": [
      "AWS Certified Solutions Architect – Associate",
      "Microsoft Certified: Azure Fundamentals",
      "(ISC)² Certified in Cybersecurity",
      "Cisco Certified Network Associate",
      "Oracle OCI - AI for Cloud Applications",
      "Java Full Stack Development"
    ]
  },
  "skills": {
    "programming_languages": ["Java", "Python", "C"],
    "web_development": ["HTML5", "CSS3", "JavaScript"],
    "databases": ["MySQL", "Oracle"],
    "cloud_platforms": ["AWS", "Microsoft Azure", "OCI"],
    "frameworks": ["J2EE", "Bootstrap"],
    "cybersecurity": [
      "Application Security",
      "Vulnerability Assessment & Penetration Testing",
      "Identity & Access Management",
      "Network Security"
    ],
    "devops_tools": ["Git", "GitHub"]
  },
  "projects": {
    "internship": {
      "company": "Languify",
      "role": "Software Developer Intern",
      "description": [
        "Built console-based Banking Management System in Java with MySQL.",
        "Improved performance through indexing and query tuning.",
        "Security enhanced with encryption and validation."
      ]
    },
    "applications": [
      {"name": "AI Assistant", "description": "Voice-controlled assistant with local LLMs for system automation.", "tech": ["Java", "Local LLMs", "Voice Recognition"]},
      {"name": "Student Record Management", "description": "System for managing student data and academic tracking.", "tech": ["Java", "MySQL"]}
    ],
    "web": [
      {"name": "FoodMunch", "description": "Restaurant homepage with responsive design and ordering flow.", "tech": ["HTML5", "CSS3", "JavaScript"]},
      {"name": "Portfolio Website", "description": "Fully responsive modern personal portfolio.", "tech": ["HTML5", "CSS3", "JavaScript"]}
    ],
    "cybersecurity_iot": [
      {"name": "Brute Force Attack Simulation & Detection", "description": "Simulation using Kali tools with SIEM-based detection.", "tech": ["Kali Linux", "Hydra", "Python", "SIEM"]},
      {"name": "Electricity Theft Detection System", "description": "Arduino-based IoT system with GSM alerts and SQL logging.", "tech": ["C", "Arduino", "GSM Module", "SQL"]}
    ]
  },
  "contact": {
    "message": "Ready to transform your digital vision into reality?",
    "links": {
      "LinkedIn": "https://www.linkedin.com/in/taahier/",
      "Email": "mailto:taahier75@gmail.com",
      "WhatsApp": "https://wa.me/917702100311",
      "GitHub": "https://github.com/taahier",
      "Resume": "https://drive.google.com/file/d/1-OMCjqSpkfJ89LWV3_xjPoya69ePylxy/view",
      "Twitter": "https://twitter.com/your_twitter_handle"
    }
  }
}

@app.get("/")
async def root():
  return {"message": "Portfolio API is running"}

@app.get("/test")
def test():
    return {"status": "ok"}

@app.get("/content")
def get_content():
    return CONTENT
