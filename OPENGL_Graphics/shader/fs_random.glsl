float random(vec2 UV)
{
    return fract(135711.0*sin(14.337*UV.x+ 52.418*UV.y));
}

in vec2 UV;
out vec4 fragColor;

void main()
{
    float r=random(UV);
    fragColor=vec4(r,r,r,1);
}