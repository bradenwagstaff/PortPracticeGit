 using UnityEngine;
 using System.Collections;
 using UnityEngine.UI;
 using TMPro;
 
 public class showFPS : MonoBehaviour {
     public TMP_Text fpsText;
     public float deltaTime;
     public int FPS = 24;
 
    void Start()
    {}

     void Update () {
         deltaTime += (Time.deltaTime - deltaTime) * 0.1f;
         float fps = 1.0f / deltaTime;
         fpsText.text = Mathf.Ceil (fps).ToString ();
     }
 }