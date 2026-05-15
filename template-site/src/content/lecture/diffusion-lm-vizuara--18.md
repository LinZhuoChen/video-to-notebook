---
course_slug: diffusion-lm-vizuara
idx: 18
title: 'Lecture 17: Diffusion LLM Coded from Scratch Part 2'
video_url: https://www.youtube.com/watch?v=UxiCIYBhH-Y
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.83
  end_sec: 56.64
  text: 'So here you can see the file which has So here you can see the file which
    has

    been loaded on runpod. Earlier I was been loaded on runpod. Earlier I was been
    loaded on runpod. Earlier I was

    getting some error but now it has run getting some error but now it has run getting
    some error but now it has run

    pretty well. And uh the same approach as pretty well. And uh the same approach
    as pretty well. And uh the same approach as

    we saw on Google collab works here. And we saw on Google collab works here. And
    we saw on Google collab works here. And

    uh you''ll see the gif being printed uh you''ll see the gif being printed uh you''ll
    see the gif being printed

    right on the screen in this code. And right on the screen in this code. And right
    on the screen in this code. And

    this uh fancy neon style gif also can be this uh fancy neon style gif also can
    be this uh fancy neon style gif also can be

    seen over here. This does not work very seen over here. This does not work very
    seen over here. This does not work very

    well right now but you can tweak the well right now but you can tweak the well
    right now but you can tweak the

    code with the help of claude or chat GPT code with the help of claude or chat
    GPT code with the help of claude or chat GPT

    to get this neon style gif to work. to get this neon style gif to work. to get
    this neon style gif to work.

    All right. So here what I''ve done is All right. So here what I''ve done is All
    right. So here what I''ve done is

    that I have just mentioned the model to that I have just mentioned the model to
    that I have just mentioned the model to

    go ahead for uh go ahead for uh go ahead for uh

    around 200,000 iterations and uh if you around 200,000 iterations and uh if you
    around 200,000 iterations and uh if you

    go ahead for these many number of go ahead for these many number of go ahead for
    these many number of

    iterations you''ll definitely see samples iterations you''ll definitely see samples'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 1
  start_sec: 56.64
  end_sec: 97.84
  text: 'iterations you''ll definitely see samples

    which are as co inference samples which which are as co inference samples which
    which are as co inference samples which

    are as coherent as what you are seeing are as coherent as what you are seeing
    are as coherent as what you are seeing

    on the screen right now. on the screen right now. on the screen right now.

    The reason I''m showing runpod to you The reason I''m showing runpod to you The
    reason I''m showing runpod to you

    along with Google collab is because along with Google collab is because along
    with Google collab is because

    uh runpod also allows you to chain uh runpod also allows you to chain uh runpod
    also allows you to chain

    multiple GPUs together and in run you multiple GPUs together and in run you multiple
    GPUs together and in run you

    can also see the different GPUs which can also see the different GPUs which can
    also see the different GPUs which

    are available whereas on Google collab are available whereas on Google collab
    are available whereas on Google collab

    if you see you''re kind of restricted if you see you''re kind of restricted if
    you see you''re kind of restricted

    right by the GPUs which they give. So if right by the GPUs which they give. So
    if right by the GPUs which they give. So if

    you go to run type you''ll see you have you go to run type you''ll see you have
    you go to run type you''ll see you have

    H100 A100 you can''t see the H100 A100 you can''t see the H100 A100 you can''t
    see the

    specifications it''s really like a black specifications it''s really like a black
    specifications it''s really like a black

    box but on the run pod you can see the box but on the run pod you can see the
    box but on the run pod you can see the

    VRAM of each GPU you can see the number VRAM of each GPU you can see the number
    VRAM of each GPU you can see the number

    of GPUs available you can see the cost of GPUs available you can see the cost
    of GPUs available you can see the cost

    you can even chain different GPUs you can even chain different GPUs'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 2
  start_sec: 97.84
  end_sec: 156.16
  text: 'you can even chain different GPUs

    together to do distributed computing if together to do distributed computing if
    together to do distributed computing if

    possible possible possible

    so let''s actually pause this right now so let''s actually pause this right now
    so let''s actually pause this right now

    let''s interrupt this after 500 let''s interrupt this after 500 let''s interrupt
    this after 500

    iterations S and uh yeah then we just iterations S and uh yeah then we just iterations
    S and uh yeah then we just

    have the sampling code over here have the sampling code over here have the sampling
    code over here

    once we have the sample here you''ll see once we have the sample here you''ll
    see once we have the sample here you''ll see

    the sampling is pretty bad because I the sampling is pretty bad because I the
    sampling is pretty bad because I

    only run for 500 iterations so that''s only run for 500 iterations so that''s
    only run for 500 iterations so that''s

    natural natural natural

    um and in this next piece of code you''ll and in this next piece of code you''ll

    save the GIF and after you save the GIF save the GIF and after you save the GIF
    save the GIF and after you save the GIF

    then you''ll print the GIF. So this code then you''ll print the GIF. So this code
    then you''ll print the GIF. So this code

    will save the GIF as inference.jif and will save the GIF as inference.jif and
    will save the GIF as inference.jif and

    this will uh essentially print it on the this will uh essentially print it on
    the this will uh essentially print it on the

    screen screen screen

    right now. Right now I''m only doing for right now. Right now I''m only doing
    for right now. Right now I''m only doing for

    500 iterations but you see already the 500 iterations but you see already the
    500 iterations but you see already the

    GIF is appearing on the screen. We don''t GIF is appearing on the screen. We don''t
    GIF is appearing on the screen. We don''t

    get that error which I was getting get that error which I was getting get that
    error which I was getting

    before. Um yeah if you train for 200,000 before. Um yeah if you train for 200,000'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 3
  start_sec: 156.16
  end_sec: 203.84
  text: 'before. Um yeah if you train for 200,000

    iterations you''ll see an amazing iterations you''ll see an amazing iterations
    you''ll see an amazing

    coherent language diffusion language coherent language diffusion language coherent
    language diffusion language

    model working from scratch as I''m model working from scratch as I''m model working
    from scratch as I''m

    showing on the screen right now. showing on the screen right now. showing on the
    screen right now.

    I''ll share the entire code file with I''ll share the entire code file with I''ll
    share the entire code file with

    you. You''ll also now be able to you. You''ll also now be able to you. You''ll
    also now be able to

    understand this large language diffusion understand this large language diffusion
    understand this large language diffusion

    models paper in a lot of depth because models paper in a lot of depth because
    models paper in a lot of depth because

    we have implemented this right from we have implemented this right from we have
    implemented this right from

    scratch. They also have a section of scratch. They also have a section of scratch.
    They also have a section of

    fine-tuning towards the end which you fine-tuning towards the end which you fine-tuning
    towards the end which you

    can easily do can easily do can easily do

    after you have finished the after you have finished the after you have finished
    the

    pre-training. You just have to assemble pre-training. You just have to assemble
    pre-training. You just have to assemble

    a fine fine tuning data set and then run a fine fine tuning data set and then
    run a fine fine tuning data set and then run

    fine tuning on top of it. So let me just fine tuning on top of it. So let me just
    fine tuning on top of it. So let me just

    Yeah. Yeah. Yeah.

    So as I mentioned this paper also So as I mentioned this paper also So as I mentioned
    this paper also

    includes fine-tuning. I have not includes fine-tuning. I have not includes fine-tuning.
    I have not

    included fine-tuning in this journey included fine-tuning in this journey included
    fine-tuning in this journey

    because I believe pre-training involves because I believe pre-training involves
    because I believe pre-training involves

    all the necessary things which you will all the necessary things which you will'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 4
  start_sec: 203.84
  end_sec: 259.509
  text: 'all the necessary things which you will

    need to learn about language diffusion need to learn about language diffusion
    need to learn about language diffusion

    models. All right. So yeah we have this All right. So yeah we have this

    traditional ARM language model code traditional ARM language model code traditional
    ARM language model code

    which runs and predicts sequential which runs and predicts sequential which runs
    and predicts sequential

    output which is coherent. And we have output which is coherent. And we have output
    which is coherent. And we have

    this uh this uh this uh

    diffusion model based language model diffusion model based language model diffusion
    model based language model

    code which predicts output such as this code which predicts output such as this
    code which predicts output such as this

    which is much faster in inference but which is much faster in inference but which
    is much faster in inference but

    pre-training might take more time. So as pre-training might take more time. So
    as pre-training might take more time. So as

    Andre Karpati mentioned in this tweet Andre Karpati mentioned in this tweet Andre
    Karpati mentioned in this tweet

    diffusion language models actually can diffusion language models actually can
    diffusion language models actually can

    be a frontier milestone in the future be a frontier milestone in the future be
    a frontier milestone in the future

    because why do we have to stick with because why do we have to stick with because
    why do we have to stick with

    auto reggressive models right of course. auto reggressive models right of course.
    auto reggressive models right of course.

    So uh I believe this is one of the first So uh I believe this is one of the first
    So uh I believe this is one of the first

    tutorials or one of the first journey tutorials or one of the first journey tutorials
    or one of the first journey

    videos which shows how to build a small videos which shows how to build a small
    videos which shows how to build a small

    scale diffusion model fully from scratch scale diffusion model fully from scratch
    scale diffusion model fully from scratch

    and I hope this codebase which I''ve and I hope this codebase which I''ve and
    I hope this codebase which I''ve

    shown on the screen right now serves as'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 5
  start_sec: 259.509
  end_sec: 308.88
  text: 'shown on the screen right now serves as shown on the screen right now serves
    as

    a reference for you to build multiple a reference for you to build multiple a
    reference for you to build multiple

    such small language models from scratch. such small language models from scratch.
    such small language models from scratch.

    So the cool thing about diffusion models So the cool thing about diffusion models
    So the cool thing about diffusion models

    is that the space is wide open, right? is that the space is wide open, right?
    is that the space is wide open, right?

    You can see small language models um let''s say small language models um let''s
    say small language models

    GitHub or Quel right all of these small GitHub or Quel right all of these small
    GitHub or Quel right all of these small

    language models which have been built language models which have been built language
    models which have been built

    they are auto reggressive models but the they are auto reggressive models but
    the they are auto reggressive models but the

    space for building diffusion models is space for building diffusion models is
    space for building diffusion models is

    wide open. I know [clears throat] wide open. I know [clears throat] wide open.
    I know [clears throat]

    Inception Labs which is one company Inception Labs which is one company Inception
    Labs which is one company

    which builds diffusion models which are which builds diffusion models which are
    which builds diffusion models which are

    pretty cool but I think this is closed pretty cool but I think this is closed
    pretty cool but I think this is closed

    source. source. source.

    I''m yet to know and opensource model I''m yet to know and opensource model I''m
    yet to know and opensource model

    which is as fast and as good as this which is as fast and as good as this which
    is as fast and as good as this

    mercury model. So you see their whole uh mercury model. So you see their whole
    uh mercury model. So you see their whole uh

    value proposition is blazing fast value proposition is blazing fast value proposition
    is blazing fast

    inference with frontier quality and a inference with frontier quality and a inference
    with frontier quality and a

    fraction of the cost which might be fraction of the cost which might be'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 6
  start_sec: 308.88
  end_sec: 324.56
  text: 'fraction of the cost which might be

    awesome for the future. But now you know awesome for the future. But now you know
    awesome for the future. But now you know

    how to build this fully yourself. Um, okay. After this, I''ll make a final okay.
    After this, I''ll make a final

    conclusion video on my thoughts and conclusion video on my thoughts and conclusion
    video on my thoughts and

    we''ll wrap it up.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
---
# Lecture 17: Diffusion LLM Coded from Scratch Part 2

See the structured chunks above.
