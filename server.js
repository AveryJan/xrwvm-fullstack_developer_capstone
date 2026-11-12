const http=require('node:http');
http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');
 if(req.method!=='GET'||!url.pathname.startsWith('/analyze/')){res.writeHead(404);return res.end('Not found');}
 const review=decodeURIComponent(url.pathname.slice('/analyze/'.length));
 const negative=/\b(bad|terrible|awful|poor|horrible|slow|worst)\b/i.test(review);
 const positive=/\b(fantastic|great|excellent|good|amazing|love|best)\b/i.test(review);
 const sentiment=negative?'negative':positive?'positive':'neutral';
 res.writeHead(200,{'Content-Type':'application/json','Access-Control-Allow-Origin':'*'});
 res.end(JSON.stringify({text:review,sentiment}));
}).listen(process.env.PORT||5050,'0.0.0.0',()=>console.log('Sentiment API listening on port '+(process.env.PORT||5050)));
