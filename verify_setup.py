import sys
import platform

print("=" * 50)
print("CADQUERY ENVIRONMENT VERIFICATION SCRIPT")
print("=" * 50)

print(f"[*] Operating System: {platform.system()} ({platform.release()})")
print(f"[*] Processor/Arch:   {platform.processor()} ({platform.machine()})")
print(f"[*] Python Version:   {sys.version.split()[0]}")

dependencies_ok = True

try:
    import cadquery as cq
    print("[✓] CadQuery:         Successfully imported")
except ImportError:
    print("[X] CadQuery:         NOT FOUND. Please make sure the 'cadquery_assignment' environment is active.")
    dependencies_ok = False

try:
    import ocp_vscode
    print("[✓] ocp-vscode:       Successfully imported")
except ImportError:
    print("[X] ocp-vscode:       NOT FOUND. Run 'pip install ocp-vscode' in your active environment.")
    dependencies_ok = False

if not dependencies_ok:
    print("\n Setup Verification Failed: Missing dependencies. Review the README installation steps.")
    sys.exit(1)

print("\n[*] Generating verification 3D model...")
try:
    verification_shape = (
        cq.Workplane("XY")
        .box(30, 30, 5)
        .faces(">Z")
        .workplane()
        .text("CQ OK", 5, 2)
    )
    
    print("[✓] 3D Engine:        B-Rep geometry generated cleanly")
    print("\n[*] Pushing to VS Code Viewport...")
    print("     (Make sure you clicked the OCP CAD Viewer icon on the left sidebar first!)")
    
    ocp_vscode.show(verification_shape)
    print("\n SUCCESS! If you see a green square token with 'CQ OK' in your viewer, your environment is perfect.")

except Exception as e:
    print(f"\n Error during rendering pipeline: {str(e)}")
    print("\n Troubleshooting Tips for Apple Silicon Macs:")
    print("   - Ensure your VS Code Python Interpreter is pointing directly to your conda/mamba env, NOT the system python.")
    print("   - If you see a symbol collision error, destroy the environment and re-create it strictly using 'mamba' to ensure ARM64 binaries match.")
    sys.exit(1)
