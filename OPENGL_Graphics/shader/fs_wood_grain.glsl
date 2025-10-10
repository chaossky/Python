float random(vec2 UV)
{
    return fract(235711.0*sin(14.337*UV.x+ 52.418*UV.y));
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

float fractalRandom(vec2 UV, float scale)
{
    float value=0.0;
    float amplitude=0.5;
    
    for (int i=0;i<6;i++)
    {
        value+=amplitude*smoothRandom(UV,scale);
        scale*=2.0;
        amplitude*=0.75;
    }
    return value;
}

in vec2 UV;
out vec4 fragColor;

void main()
{
    float t=80*UV.y+20*fractalRandom(UV,2);
    float r=clamp(2*abs(sin(t)),0,1);
    vec4 color1=vec4(0.3,0.2,0.0,1.0);
    vec4 color2=vec4(0.6,0.4,0.2,1.0);
    
    fragColor=mix(color1,color2,r);
}