import { useEffect,useState } from "react";
import API from "../services/api";

function Dashboard(){

 const [tasks,setTasks]=useState([]);
 const [title,setTitle]=useState("");
 const [description,setDescription]=useState("");

 const token=localStorage.getItem(
   "token"
 );

 const loadTasks=async()=>{

  const res=await API.get(
   "/tasks",
   {
    headers:{
     Authorization:`Bearer ${token}`
    }
   }
  );

  setTasks(res.data);
 };

 useEffect(()=>{
  loadTasks();
 },[]);

 const addTask=async()=>{

  await API.post(
   "/tasks",
   {
    title,
    description
   },
   {
    headers:{
     Authorization:`Bearer ${token}`
    }
   }
  );

  loadTasks();
 };

 return(
 <>
  <h1>Dashboard</h1>

  <input
   placeholder="Title"
   onChange={(e)=>
   setTitle(e.target.value)}
  />

  <input
   placeholder="Description"
   onChange={(e)=>
   setDescription(e.target.value)}
  />

  <button onClick={addTask}>
   Add Task
  </button>

  {
   tasks.map(task=>(
    <div key={task.id}>
      <h3>{task.title}</h3>
      <p>{task.description}</p>
    </div>
   ))
  }
 </>
 );
}

export default Dashboard;