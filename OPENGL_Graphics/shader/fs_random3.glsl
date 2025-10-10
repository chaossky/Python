float random(vec2 UV)
{
    return fract(135711.0*sin(14.337*UV.x+ 52.418*UV.y));
}

float boxRandom(vec2 UV,float scale)
{
    vec2 iScaleUV=floor(UV*scale);
    return random(iScaleUV);
}

float smoothRandom(vec2 UV, float scale)
{
    vec2 iScaleUV = floor(scale * UV);
    vec2 fScaleUV = fract(scale * UV);  // 수정된 부분
    float a = random(iScaleUV);
    float b = random(round(iScaleUV + vec2(1, 0)));
    float c = random(round(iScaleUV + vec2(0, 1)));
    float d = random(round(iScaleUV + vec2(1, 1))); 
    return mix(mix(a, b, fScaleUV.x), mix(c, d, fScaleUV.x), fScaleUV.y);
}

in vec2 UV;
out vec4 fragColor;

void main()
{
    //float r=boxRandom(UV,20);
    float r=smoothRandom(UV,10);
    //float t=fractalRandom(UV,4);
    //float r=abs(sin(20*t));
    //vec4 color1=vec4(0,0.2,0,1);
    //vec4 color2=vec4(1,1,1,1);
    
    //fragColor=mix(color1,color2,r);

    fragColor=vec4(r,r,r,1);
}