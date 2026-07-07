async function send(){

    let message=document.getElementById("msg").value;

    let res=await fetch("http://127.0.0.1:8000/chat",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            session_id:"demo",

            persona:"chro",

            message:message

        })

    });

    let data=await res.json();

    document.getElementById("chat").innerHTML+=`

<p><b>You:</b> ${message}</p>

<p><b>AI:</b> ${data.assistant_message}</p>

`;

}