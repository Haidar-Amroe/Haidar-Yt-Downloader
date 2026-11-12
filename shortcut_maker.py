import os
import subprocess
import sys

def create_desktop_shortcut():
    # Automatically finds the path of yt_downloader.py in the same folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, "yt_downloader.py")
    
    if not os.path.exists(script_path):
        print(f"[ERROR] Could not find 'yt_downloader.py' in {current_dir}")
        return

    # Automatically gets your Desktop path and Python executable path
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    shortcut_path = os.path.join(desktop_dir, "YouTube Downloader.lnk")
    python_exe = sys.executable

    # Create a temporary VBScript to generate a native Windows .lnk shortcut
    vbs_script = f"""
    Set oWS = WScript.CreateObject("WScript.Shell")
    sLinkFile = "{shortcut_path}"
    Set oLink = oWS.CreateShortcut(sLinkFile)
    oLink.TargetPath = "{python_exe}"
    oLink.Arguments = """"{script_path}""""
    oLink.WorkingDirectory = "{current_dir}"
    oLink.Description = "YouTube Video Downloader (MP4)"
    oLink.Save
    """

    vbs_path = os.path.join(current_dir, "temp_shortcut.vbs")
    
    try:
        with open(vbs_path, "w") as f:
            f.write(vbs_script)
        
        # Execute the VBScript
        subprocess.run(["cscript", "//nologo", vbs_path], check=True)
        print(f"[SUKSES] Shortcut berhasil dibuat di Desktop: {shortcut_path}")
        
    except Exception as e:
        print(f"[ERROR] Gagal membuat shortcut: {e}")
        
    finally:
        # Clean up the temporary VBScript file
        if os.path.exists(vbs_path):
            os.remove(vbs_path)

if __name__ == "__main__":
    create_desktop_shortcut()