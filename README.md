# FileDumper - Memory Forensic Dumper

**FileDumper v1.0.1**  
A simple, powerful tool to dump files directly from process memory regions.  

Created in a late-night collaboration between **human ingenuity** and **AI creativity** —  
xAI's Grok + Kadir Isbirligi (2026)  

> "Bir gece sohbet ettik, kod yazdık, masaya yumruk vurduk...  
> İnsan + AI = Sonsuz güç!"

### What is this?
FileDumper is a Windows-based memory forensics tool that can:
- List active processes
- Show process info (CPU/memory usage)
- Suspend / Resume processes
- Search & dump memory regions matching a specific byte pattern (e.g. file signatures like PDF, JPG, SWF, etc.)
- Save dumped memory chunks as `.bin` files for further analysis

Perfect for quick & dirty memory forensics, file carving from RAM, or just messing around.

### Features Showcase

Here are some screenshots showing the tool in action:

**Beautiful ASCII banner & usage/help screen**  
![Banner and Help](screenshots/ss1.png)  <!-- Senin ss1 için -->

**Dumped .bin files in folder**  
![Dumped Files](screenshots/ss2.png)  <!-- ss2 için -->

**Hex + ASCII memory dump view**  
![Hex Dump](screenshots/ss3.png)  <!-- ss3 için -->

**Process list output**  
![Process List](screenshots/ss4.png)  <!-- ss4 için -->

**Help screen with commands**  
![Help Commands](screenshots/ss5.png)  <!-- ss5 için -->

**More process list**  
![Process List Continued](screenshots/ss6.png)  <!-- ss6 için -->

**Dumping in action with success messages**  
![Dumping Output](screenshots/ss7.png)  <!-- ss7 için -->

### Requirements

- **Windows** operating system (tested on Win10/11)
- **Python 2.7** (as shown in screenshots; Python 3 compatibility not tested yet)
- **Administrator privileges** (must run as admin!)
- Required packages:

```bash
pip install psutil>=6.0.0
pip install memorpy   # usually installed from git: https://github.com/n1nj4sec/memorpy


Note: If pip complains about versions, use Python 2 compatible ones. memorpy might need manual install from source if issues aris


Installation & Quick Start
Clone or download the repo
Install dependencies (see above)
Run as Administrator:

python2 filedumper.py list                  # List all processes
python2 filedumper.py info --pid 1234       # Show info about specific process
python2 filedumper.py suspend --pid 1234    # Freeze the process
python2 filedumper.py dump --pid 1234 --pattern "\xAB\x00\x0C"   # Dump matching regions
python2 filedumper.py resume --pid 1234     # Resume after dumping


Important Warnings
Antivirus will most likely flag this tool (false-positive). Add exception.
Suspending random processes can crash your system or applications — use with care!
Dumping memory requires admin rights and can be detected by EDR solutions.
You are responsible for what you do with this tool. We just built it for fun and learning.
We did our part — now it's yours.

Made with 🤖 + 👨‍💻 in 2026
xAI Grok & Kadir
