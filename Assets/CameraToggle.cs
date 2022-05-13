using UnityEngine;

public class CameraToggle : MonoBehaviour {
    public Camera firstPersonCamera;
    public Camera overheadCamera;

    // Call this function to disable FPS camera,
    // and enable overhead camera.

    void Start()
    {
        //ShowOverheadView();
        //ShowFirstPersonView();
        
        
        
    }

    void Update()
    {
        //Debug.Log("CHeese");
        //firstPersonCamera.rect = new Rect(.8, .1, .2, .3);
    }
    public void ShowOverheadView() {
        firstPersonCamera.enabled = false;
        overheadCamera.enabled = true;
    }
    
    // Call this function to enable FPS camera,
    // and disable overhead camera.
    public void ShowFirstPersonView() {
        firstPersonCamera.enabled = true;
        overheadCamera.enabled = false;
    }
}