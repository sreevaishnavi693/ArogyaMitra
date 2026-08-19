import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

const api = import.meta.env.VITE_API_URL || 'http://localhost:8000';
const initial = { name: 'Vaishnavi', goal: 'Weight Loss', location: 'Home', minutes_per_day: 30, fitness_level: 'Beginner', dietary_preference: 'Vegetarian', allergies: ['peanuts'], health_notes: '' };

function App() {
  const [profile, setProfile] = useState(initial);
  const [data, setData] = useState(null);
  const [tab, setTab] = useState('Today');
  const [coach, setCoach] = useState('I am traveling for 4 days');
  const [reply, setReply] = useState('');
  const update = e => setProfile({ ...profile, [e.target.name]: e.target.name === 'minutes_per_day' ? Number(e.target.value) : e.target.value });
  const createPlan = async () => { const res = await fetch(`${api}/api/plans`, { method: 'POST', headers: { 'Content-Type':'application/json' }, body: JSON.stringify(profile) }); setData(await res.json()); setTab('Plan'); };
  const askCoach = async () => { const res = await fetch(`${api}/api/coach`, { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({message:coach}) }); setReply((await res.json()).reply); };
  return <main><header><div><span className="eyebrow">AROGYAMITRA</span><h1>Wellness that adapts to your life.</h1><p>Your mindful AI companion for movement, meals, and momentum.</p></div><button onClick={createPlan}>Generate my 7-day plan</button></header>
  <nav>{['Today','Plan','Meals','AROMI'].map(x => <button className={tab===x?'active':''} onClick={()=>setTab(x)} key={x}>{x}</button>)}</nav>
  {tab==='Today' && <section className="grid"><article className="hero-card"><span>GOOD MORNING, {profile.name.toUpperCase()}</span><h2>One healthy decision at a time.</h2><p>Today: a {profile.minutes_per_day}-minute {profile.location.toLowerCase()} session built around your {profile.goal.toLowerCase()} goal.</p><button onClick={createPlan}>Start today’s session</button></article><article><h3>Set your rhythm</h3><label>Goal<select name="goal" value={profile.goal} onChange={update}><option>Weight Loss</option><option>Strength</option><option>Mobility</option><option>General Wellness</option></select></label><label>Where<select name="location" value={profile.location} onChange={update}><option>Home</option><option>Gym</option><option>Outdoors</option></select></label><label>Minutes <input type="number" name="minutes_per_day" value={profile.minutes_per_day} onChange={update}/></label></article><article><h3>This week</h3><div className="rings"><b>3</b><span>movement days</span></div><p>Hydration streak: 2 days</p><p>Small steps compound. Keep going.</p></article></section>}
  {tab==='Plan' && <section><h2>Your 7-day movement plan</h2>{data ? <div className="cards">{data.workouts.map(x=><article key={x.day}><span>{x.day} · {x.intensity}</span><h3>{x.title}</h3><p>{x.duration} · {x.focus}</p><ul>{x.exercises.map(e=><li key={e}>{e}</li>)}</ul></article>)}</div> : <Empty onClick={createPlan}/>}</section>}
  {tab==='Meals' && <section><h2>Simple, nourishing meals</h2>{data ? <div className="cards">{data.meals.map(x=><article key={x.day}><span>{x.day}</span><h3>{x.breakfast}</h3><p><b>Lunch:</b> {x.lunch}</p><p><b>Dinner:</b> {x.dinner}</p><small>{x.note}</small></article>)}</div> : <Empty onClick={createPlan}/>}</section>}
  {tab==='AROMI' && <section className="coach"><span className="orb">A</span><div><span className="eyebrow">YOUR ADAPTIVE COACH</span><h2>Hi, I’m AROMI.</h2><p>Tell me what changed, and I’ll help make today’s plan doable.</p><textarea value={coach} onChange={e=>setCoach(e.target.value)}/><button onClick={askCoach}>Ask AROMI</button>{reply && <blockquote>{reply}</blockquote>}</div></section>}
  </main>;
}
function Empty({onClick}) { return <article className="empty"><p>Generate your personalized plan to see it here.</p><button onClick={onClick}>Generate plan</button></article> }
createRoot(document.getElementById('root')).render(<App/>);

