/*let d = [[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]]
const message = document.getElementById("messages");

for(let i = 0; i < d.length; i++){
    let div = document.createElement('div');
    div.classList.add("met");
    for(let j = 0; j < d[i].length; j++){
        let para = document.createElement('p')
        para.innerHTML = d[i][j];
        para.style.color = 'rgb(0,0,255)';
        div.appendChild(para)
    }
    message.appendChild(div);
}*/
/*
const message = document.getElementById("messages");
for(let i = 0; i < 5; i++){
    let d= document.createElement('div');
    d.classList.add("d");
    for(let j = 0; j < 10; j++){
        let div= document.createElement('div');
        div.classList.add("met");
        for(let k = 0; k < 10; k++){
            let para = document.createElement('p');
            para.innerHTML = "@"
            div.appendChild(para)
        }
        d.appendChild(div);
    }
    message.innerHTML = '';
    message.appendChild(d);
    
    
}*/

const source = new EventSource("/stream");
const message = document.getElementById("messages");
source.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const y= document.createElement('div');
    y.classList.add("group");
    for(let i = 0; i < data.color.length; i++){
        let div = document.createElement('div');
        div.classList.add("met");
        for(let j = 0; j < data.color[i].length; j++){
            const para = document.createElement('p');
            para.innerHTML = "@";
            para.style.color = `rgb(${data.color[i][j][0]},${data.color[i][j][1]},${data.color[i][j][2]})`;
            div.appendChild(para);
        }
        
            y.appendChild(div);
    }
    message.innerHTML = '';
    message.appendChild(y);
    
    
};

