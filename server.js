const http=require('node:http');
const states=['Kansas','Illinois','California','Texas','New York'];
const cities=['Wichita','Chicago','Los Angeles','Austin','Albany'];
const dealers=Array.from({length:50},(_,i)=>({id:i+1,city:cities[i%5],state:states[i%5],address:`${100+i} Commerce Road`,zip:String(66000+i),lat:37.5+(i%5),long:-97.3-(i%5),short_name:`Demo Dealer ${i+1}`,full_name:`Best Cars Demo Dealership ${i+1}`}));
const reviews=[{id:1,dealerId:1,name:'Example Reviewer',review:'Fantastic services',purchase:true,car_make:'Toyota',car_model:'Camry',car_year:2024}];
const send=(res,status,obj)=>{res.writeHead(status,{'Content-Type':'application/json','Access-Control-Allow-Origin':'*','Access-Control-Allow-Headers':'Content-Type','Access-Control-Allow-Methods':'GET,POST,OPTIONS'});res.end(JSON.stringify(obj));};
http.createServer((req,res)=>{
 if(req.method==='OPTIONS')return send(res,204,{});
 const pathname=new URL(req.url,'http://localhost').pathname;
 if(req.method==='GET'&&pathname==='/fetchDealers')return send(res,200,dealers);
 let m=pathname.match(/^\/fetchDealers\/([^/]+)$/);
 if(req.method==='GET'&&m)return send(res,200,dealers.filter(d=>d.state.toLowerCase()===decodeURIComponent(m[1]).toLowerCase()));
 m=pathname.match(/^\/fetchDealer\/(\d+)$/);
 if(req.method==='GET'&&m){const found=dealers.find(d=>d.id===Number(m[1]));return send(res,found?200:404,found||{error:'Dealer not found'});}
 m=pathname.match(/^\/fetchReviews\/dealer\/(\d+)$/);
 if(req.method==='GET'&&m)return send(res,200,reviews.filter(r=>r.dealerId===Number(m[1])));
 if(req.method==='POST'&&pathname==='/postReview'){
  let body='';req.on('data',c=>{body+=c;if(body.length>100000)req.destroy();});req.on('end',()=>{try{const obj=JSON.parse(body);if(!dealers.some(d=>d.id===Number(obj.dealerId))||!obj.review||!obj.name)return send(res,400,{error:'Valid dealerId, name and review required'});const review={...obj,id:reviews.length+1};reviews.push(review);send(res,201,review);}catch(e){send(res,400,{error:'Invalid JSON'});}});return;
 }
 send(res,404,{error:'Not found'});
}).listen(process.env.PORT||3030,'0.0.0.0',()=>console.log('Dealer API listening on port '+(process.env.PORT||3030)));
