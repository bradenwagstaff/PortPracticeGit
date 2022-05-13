using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Net.Sockets;
using UnityEngine;

public class SocketClientUnity : MonoBehaviour
{
    public String Host = "127.0.0.1";
    public Int32 Port = 65432;
    public Transform cube;
    public Vector3 cubePosition;
    public float cubeX = 0;
    public float cubeY = 0;
    public float cubeZ = 0;
    public int FPS;
    


    TcpClient mySocket = null;
    NetworkStream theStream = null;
    StreamWriter theWriter = null;
    Byte[] sendBytes    = new Byte[1024];
    Byte[] receiveBytes = new Byte[1024];

    // Start is called before the first frame update
    void Start()
    {
        FPS = 30;
        Debug.Log(FPS);
        Application.targetFrameRate = FPS;
        QualitySettings.vSyncCount = 0;
        mySocket = new TcpClient();

        if (ConnectSocket())
        {
            Debug.Log("socket is set up");
        }
       
    }

    // Update is called once per frame
    void Update()
    {
        FPS = 30;
        // Debug.Log(FPS);
        Application.targetFrameRate = FPS;
        QualitySettings.vSyncCount = 0;
        if (!mySocket.Connected)
        {
            ConnectSocket();
        } else
        {
            RunSocket();
        }
       
    }
    public bool ConnectSocket() {
        try
        {
            mySocket.Connect(Host, Port);
            theStream = mySocket.GetStream();
            theWriter = new StreamWriter(theStream);
            return true;
        }
        catch
        {
            return false;
        }
    }
    public bool RunSocket()
    {
        try
        {
            sendBytes = System.Text.Encoding.UTF8.GetBytes(FPS.ToString());
            receiveBytes = new Byte[1024];
            mySocket.GetStream().Write(sendBytes, 0, sendBytes.Length);
            //Debug.Log("socket is sent");
            mySocket.GetStream().Read(receiveBytes, 0, 1024);
            //Debug.Log((float.Parse((((float)System.BitConverter.ToSingle(receiveBytes, 0 * sizeof(float))).ToString()))).GetType());
            cubeX = (float.Parse((((float)System.BitConverter.ToSingle(receiveBytes, 0 * sizeof(float))).ToString())));
            cubeY = (float.Parse((((float)System.BitConverter.ToSingle(receiveBytes, 1 * sizeof(float))).ToString())));
            cubeZ = (float.Parse((((float)System.BitConverter.ToSingle(receiveBytes, 2 * sizeof(float))).ToString())));
            Debug.Log(cubeY);
            cubePosition.Set(cubeX, cubeY, cubeZ);
            cube.position += cubePosition * Time.deltaTime;

            return true;
        }
        catch (Exception e)
        {
            Debug.Log("Socket error: " + e);
            return false;
        }
    }
    private void OnApplicationQuit()
    {
        if (mySocket != null && mySocket.Connected)

            mySocket.Close();
    }
}
