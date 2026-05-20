---
course_slug: diffusion-lm-vizuara
idx: 1
title: Build a Diffusion Language Model from Scratch Workshop
video_url: https://www.youtube.com/watch?v=9Q9qS48PyLA
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.149
  end_sec: 71.68
  text: 'All of you love the build large language All of you love the build large
    language

    models from scratch cars which we have models from scratch cars which we have
    models from scratch cars which we have

    on YouTube. on YouTube. on YouTube.

    Those were auto reggressive models which Those were auto reggressive models which
    Those were auto reggressive models which

    predict one token at a time. Now I''m predict one token at a time. Now I''m predict
    one token at a time. Now I''m

    coming up with a new series of lectures coming up with a new series of lectures
    coming up with a new series of lectures

    in which I''m going to teach you how to in which I''m going to teach you how to
    in which I''m going to teach you how to

    build a diffusion language model build a diffusion language model build a diffusion
    language model

    entirely from scratch. Hello everyone. This is Dr. Raj Gandhar, Hello everyone.
    This is Dr. Raj Gandhar,

    one of the three co-founders of Vijara one of the three co-founders of Vijara
    one of the three co-founders of Vijara

    AI Labs. Today I''m very excited to AI Labs. Today I''m very excited to AI Labs.
    Today I''m very excited to

    announce the launch of our new workshop, announce the launch of our new workshop,
    announce the launch of our new workshop,

    build a diffusion language model from build a diffusion language model from build
    a diffusion language model from

    scratch. I have been working on this for scratch. I have been working on this
    for scratch. I have been working on this for

    the past five to 6 months and I''m the past five to 6 months and I''m the past
    five to 6 months and I''m

    finally ready with this uh series of finally ready with this uh series of finally
    ready with this uh series of

    lectures. lectures. lectures.

    So in 2025 So in 2025 So in 2025

    the state-ofthe-art for language models the state-ofthe-art for language models
    the state-ofthe-art for language models

    was auto reggressive language models was auto reggressive language models was
    auto reggressive language models

    which predicted one new token at a time. which predicted one new token at a time.
    which predicted one new token at a time.

    Then there was a flurry of diffusion Then there was a flurry of diffusion'
  concept_slugs:
  - diffusion-language-model
- idx: 1
  start_sec: 71.68
  end_sec: 136.56
  text: 'Then there was a flurry of diffusion

    based models which were released. based models which were released. based models
    which were released.

    Essentially think of diffusion as Essentially think of diffusion as Essentially
    think of diffusion as

    instead of one token at a time, it instead of one token at a time, it instead
    of one token at a time, it

    predicts all the text at once. Like in predicts all the text at once. Like in
    predicts all the text at once. Like in

    the video which you see here. So when we when I saw this video or when So when
    we when I saw this video or when

    I saw this GIF, it looked amazing to me. I saw this GIF, it looked amazing to
    me. I saw this GIF, it looked amazing to me.

    Yeah, why should X be produced one token Yeah, why should X be produced one token
    Yeah, why should X be produced one token

    at a time? Why cannot it just appear to at a time? Why cannot it just appear to
    at a time? Why cannot it just appear to

    me like diffusion based models for me like diffusion based models for me like
    diffusion based models for

    images? That leads to much faster images? That leads to much faster images? That
    leads to much faster

    inference times, right? And then I went inference times, right? And then I went
    inference times, right? And then I went

    on a journey to learn how to build this on a journey to learn how to build this
    on a journey to learn how to build this

    diffusion language model fully from diffusion language model fully from diffusion
    language model fully from

    scratch. scratch. scratch.

    How can I understand the nuts and bolts How can I understand the nuts and bolts
    How can I understand the nuts and bolts

    of how the entire architecture of the of how the entire architecture of the of
    how the entire architecture of the

    diffusion language model was assembled? diffusion language model was assembled?
    diffusion language model was assembled?

    There was very little information There was very little information There was
    very little information

    online. It was very difficult to find online. It was very difficult to find online.
    It was very difficult to find

    GitHub repositories or online videos GitHub repositories or online videos'
  concept_slugs:
  - diffusion-language-model
- idx: 2
  start_sec: 136.56
  end_sec: 194.959
  text: 'GitHub repositories or online videos

    which teach me everything I want to which teach me everything I want to which
    teach me everything I want to

    know. I did not want a 5 minute tutorial know. I did not want a 5 minute tutorial
    know. I did not want a 5 minute tutorial

    or a 10-minute tutorial. or a 10-minute tutorial. or a 10-minute tutorial.

    As I went through this journey, now I''m As I went through this journey, now I''m
    As I went through this journey, now I''m

    ready with the whole uh pipeline which I ready with the whole uh pipeline which
    I ready with the whole uh pipeline which I

    have built and I''m ready to teach it all have built and I''m ready to teach it
    all have built and I''m ready to teach it all

    to you. Initially this workshop was to you. Initially this workshop was to you.
    Initially this workshop was

    planned as uh intensive boot camp for planned as uh intensive boot camp for planned
    as uh intensive boot camp for

    industry professionals but now we are industry professionals but now we are industry
    professionals but now we are

    opening it up um for everyone. opening it up um for everyone. opening it up um
    for everyone.

    Here is the content which we will cover through this uh boot camp or through through
    this uh boot camp or through

    this workshop. On each day we will cover this workshop. On each day we will cover
    this workshop. On each day we will cover

    something different. On day one, we will something different. On day one, we will
    something different. On day one, we will

    understand the introduction to diffusion understand the introduction to diffusion
    understand the introduction to diffusion

    models and looking at generative AI models and looking at generative AI models
    and looking at generative AI

    through a probabilistic lens. On day through a probabilistic lens. On day through
    a probabilistic lens. On day

    two, we''ll understand auto reggressive two, we''ll understand auto reggressive
    two, we''ll understand auto reggressive

    models, their limitations. On day three, models, their limitations. On day three,
    models, their limitations. On day three,

    we''ll build the diffusion language model we''ll build the diffusion language
    model we''ll build the diffusion language model

    pipeline, the training pipeline, and the pipeline, the training pipeline, and
    the'
  concept_slugs:
  - diffusion-language-model
- idx: 3
  start_sec: 194.959
  end_sec: 231.04
  text: 'pipeline, the training pipeline, and the

    inference pipeline. And on day four, inference pipeline. And on day four, inference
    pipeline. And on day four,

    we''ll code the full diffusion model from we''ll code the full diffusion model
    from we''ll code the full diffusion model from

    scratch. I''ll even give you research scratch. I''ll even give you research scratch.
    I''ll even give you research

    projects at the end of this workshop projects at the end of this workshop projects
    at the end of this workshop

    which you can do on your own and you can which you can do on your own and you
    can which you can do on your own and you can

    then convert it into a publication. I then convert it into a publication. I then
    convert it into a publication. I

    think this is the first workshop in the think this is the first workshop in the
    think this is the first workshop in the

    world which teaches you how to build a world which teaches you how to build a
    world which teaches you how to build a

    diffusion language model fully from diffusion language model fully from

    scratch. The workshop starts from the scratch. The workshop starts from the scratch.
    The workshop starts from the

    2nd of February and it will finish on 2nd of February and it will finish on 2nd
    of February and it will finish on

    the 6th of February. I''m really looking the 6th of February. I''m really looking
    the 6th of February. I''m really looking

    forward to seeing you all there. So, forward to seeing you all there. So, forward
    to seeing you all there. So,

    thank you for watching and uh I hope you thank you for watching and uh I hope
    you thank you for watching and uh I hope you

    find the workshop very valuable.'
  concept_slugs:
  - diffusion-language-model
---
# Build a Diffusion Language Model from Scratch Workshop

See the structured chunks above.
