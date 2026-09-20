
const fileInput=document.getElementById("fileInput");
const uploadButton=document.getElementById("uploadButton");
const statusText=document.getElementById("status")

let departmentChart=null;
uploadButton.addEventListener("click",async()=>{
    const file=fileInput.files[0];
    if(!file){
        statusText.textContent="Please select a CSV or JSON file.";
        return;
    }
    const formData=new FormData();
    formData.append("file",file);
    statusText.textContent="Uploading and analyzing file...";
    try{
        const response=await fetch("/upload",{method:"POST",body:formData});
        const result=await response.json();
        console.log("FULL API RESULT:",result);
        console.log("API RESULT KEYS:",Object.keys(result));
        console.log("FastAPI status:",result);
        if(!response.ok || result.error){
            statusText.textContent=result.error || "Something went wrong."
            //throw new Error(`FastAPI returned HTTP ${response.status}`);
            return;
        }
        const summary=result["Statistical Summary"];
        const departmentData=result["Average Marks by Departmet"];
        const cleanedData=result["Cleaned Data"];
        console.log("Summary:",summary);
        console.log("Department data:",departmentData);
        console.log("Cleaned data:",cleanedData);
        displayStatistics(summary);
        diaplayChart(departmentData);
        displayData(cleanedData);
        statusText.textContent="File analyzed successfully.";
    
    }
    catch(error)
    {
        console.error("Dashboard error:",error);
        statusText.textContent=`Error:${error.message}`;
    }
});
function displayStatistics(summary){
    if(!summary){
        console.error("Satistical summary is missing.");
        return;
    }
    console.log("Statistics received:",summary);
    document.getElementById("count").textContent=summary.count ?? "-";
    document.getElementById("mean").textContent=summary.mean ?? "-";
    document.getElementById("median").textContent=summary.median ?? "-";
    document.getElementById("percentile25").textContent=summary["25th_percentile"] ?? "-";
    document.getElementById("percentile50").textContent=summary["50th_percentile"] ?? "-";
    document.getElementById("percentile75").textContent=summary["75th_percentile"] ?? "-";
}

function diaplayChart(groupedData)
{
    const canvas=document.getElementById("departmentChart");
    if(!canvas){
        console.error("departmentChart canvas not found.");
        return;
    }
    if(!groupedData || typeof groupedData !== "object"){
        console.error("Department data is missing:",groupedData);
        return;
    }
    const labels=Object.keys(groupedData);
    const values=Object.values(groupedData);
    console.log("Chart labels:",labels);
    console.log("Chart values:",values);
    if(departmentChart){
        departmentChart.destroy();
    }
    departmentChart=new Chart(
        canvas,
        {
            type:"bar",
            data:{
                labels:labels,
                datasets:[
                    {
                        label:"Average Marks",data:values
                    }
                ]
            },
            options:{
                responsive:true,
                maintainAspectRation:false,
                scales:{
                    y:{
                        beginAtZero:true
                    }
                }
            }
        }
    );
}

function displayData(data)
{

    const container=document.getElementById("dataContainer");
    if(!container){
        console.error("dataContainer not found");
        return;
    }
    if(!data || data.length === 0)
    {
        container.innerHTML="<p>No data available.</p>";
        return;
    }
    const columns=Object.keys(data[0]);
    let html="<table>";
    html+="<thead><tr>";
    columns.forEach(column=>{
        html+=`<th>${column}</th>`;
    });
    html+="</tr></thead>";
    html+="<tbody>";
    data.forEach(row=>{
        html+="<tr>"
        columns.forEach(column=>{
            html+=`<td>${row[column] ?? ""}</td>`;
        });
        html+="<tr>";
    });
    html+="</tbody>";
    html+="</table>";
    container.innerHTML=html;
}