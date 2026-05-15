---
course_slug: cmu-10799-diffusion-flow
idx: 4
title: 'CMU 10799 S26: Diffusion & Flow Matching - Lecture 1 - Basics of Probabilistic
  & Generative Modeling'
video_url: https://www.youtube.com/watch?v=p7Q77S_ZhdA
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.71
  end_sec: 84.479
  text: 'All right, class. Class, shall we begin? All right, class. Class, shall we
    begin?

    Shall we begin? Shall we begin? Shall we begin?

    Welcome to 10799. Welcome to 10799. Welcome to 10799.

    My name is Kelly, and in this class, My name is Kelly, and in this class, My name
    is Kelly, and in this class,

    we''re going to learn about diffusion and we''re going to learn about diffusion
    and we''re going to learn about diffusion and

    flow matching. Woohoo. flow matching. Woohoo. flow matching. Woohoo.

    All right, so All right, so All right, so

    let''s begin. The year of 2025 let''s begin. The year of 2025 let''s begin. The
    year of 2025

    is uh absolutely insane, let''s just say. is uh absolutely insane, let''s just
    say. is uh absolutely insane, let''s just say.

    So, we have great memes. um that comes So, we have great memes. um that comes
    So, we have great memes. um that comes

    from chat GPT. And then we from chat GPT. And then we from chat GPT. And then
    we

    have some like crazy good have some like crazy good have some like crazy good

    AI generated ASMR video that I uh listen AI generated ASMR video that I uh listen
    AI generated ASMR video that I uh listen

    to pretty often. to pretty often. to pretty often.

    And we also have some Yeah. And we have some weird things that Yeah. And we have
    some weird things that

    is like flowing around the internet now. is like flowing around the internet now.
    is like flowing around the internet now.

    Um yeah, so I''ve been spending hours on Um yeah, so I''ve been spending hours
    on Um yeah, so I''ve been spending hours on

    these uh memes every day. I I suppose uh these uh memes every day. I I suppose
    uh these uh memes every day. I I suppose uh

    it''s been a great year. Um it''s been a great year. Um it''s been a great year.
    Um

    who nope, not again. Okay. Absolutely. who nope, not again. Okay. Absolutely.
    who nope, not again. Okay. Absolutely.

    The best thing that happened to me in The best thing that happened to me in The
    best thing that happened to me in

    2025 will be the Italian brain rods. Uh 2025 will be the Italian brain rods. Uh'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 1
  start_sec: 84.479
  end_sec: 143.43
  text: '2025 will be the Italian brain rods. Uh

    so for those of you guys who don''t know so for those of you guys who don''t know
    so for those of you guys who don''t know

    this is this is this is

    this is bombado and this is my favorite. Um yeah so these thing are amazing like
    Um yeah so these thing are amazing like

    my best thing that ever happened to me my best thing that ever happened to me
    my best thing that ever happened to me

    in 2025. Um besides the memes right the in 2025. Um besides the memes right the
    in 2025. Um besides the memes right the

    industry is also pretty much blooming industry is also pretty much blooming industry
    is also pretty much blooming

    for this entire year. Uh that includes for this entire year. Uh that includes
    for this entire year. Uh that includes

    basically we got some like great photo basically we got some like great photo
    basically we got some like great photo

    editing um tools now that''s um available editing um tools now that''s um available
    editing um tools now that''s um available

    in Photoshop which is our traditional uh in Photoshop which is our traditional
    uh in Photoshop which is our traditional uh

    image editing app and then we have some image editing app and then we have some
    image editing app and then we have some

    like really really fast uh LMS that is like really really fast uh LMS that is
    like really really fast uh LMS that is

    going on and we can also try to do like going on and we can also try to do like
    going on and we can also try to do like

    material science or like try to do drug material science or like try to do drug
    material science or like try to do drug

    discoveries using AI in the past year. discoveries using AI in the past year.
    discoveries using AI in the past year.

    So So So

    basically all of these things that I''ve basically all of these things that I''ve
    basically all of these things that I''ve

    just showed you just now are built upon just showed you just now are built upon
    just showed you just now are built upon

    the same underlying technology and that'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 2
  start_sec: 143.43
  end_sec: 195.27
  text: 'the same underlying technology and that the same underlying technology and
    that

    is is is

    hello and that is we got stuck. Oh and that is and that is we got stuck. Oh and
    that is

    this uh diffuser um and uh that is what this uh diffuser um and uh that is what
    this uh diffuser um and uh that is what

    we''re going to learn uh in this class. we''re going to learn uh in this class.
    we''re going to learn uh in this class.

    Okay. So in this class we''re going to Okay. So in this class we''re going to
    Okay. So in this class we''re going to

    learn about diffusion and flow matching learn about diffusion and flow matching
    learn about diffusion and flow matching

    which is the tech technology that is which is the tech technology that is which
    is the tech technology that is

    behind a lot of these great memes uh or behind a lot of these great memes uh or
    behind a lot of these great memes uh or

    advancements I suppose um in image advancements I suppose um in image advancements
    I suppose um in image

    generation and beyond in the recent generation and beyond in the recent generation
    and beyond in the recent

    years. In particular years. In particular years. In particular

    we are going to be learn about the we are going to be learn about the we are going
    to be learn about the

    intuition and the math behind this intuition and the math behind this intuition
    and the math behind this

    algorithm. Uh so for those of you who algorithm. Uh so for those of you who algorithm.
    Uh so for those of you who

    probably already heard about diffusion, probably already heard about diffusion,
    probably already heard about diffusion,

    this thing is like slightly math heavy this thing is like slightly math heavy
    this thing is like slightly math heavy

    but if you get the correct intuition but if you get the correct intuition but
    if you get the correct intuition

    it''s going to be very easy to understand it''s going to be very easy to understand
    it''s going to be very easy to understand

    and also you''re going to learn how to and also you''re going to learn how to
    and also you''re going to learn how to

    implement these things um like in Python'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 3
  start_sec: 195.27
  end_sec: 246.949
  text: 'implement these things um like in Python implement these things um like in
    Python

    which is the language that we use every which is the language that we use every
    which is the language that we use every

    every day now um and also basically how every day now um and also basically how
    every day now um and also basically how

    to train a good image generation models to train a good image generation models
    to train a good image generation models

    using GPUs which is the yeah the uh the using GPUs which is the yeah the uh the
    using GPUs which is the yeah the uh the

    machines that we use to train models machines that we use to train models machines
    that we use to train models

    these days. Um, these days. Um, these days. Um,

    and after you implement the basic and after you implement the basic and after
    you implement the basic

    algorithms, you''re going to also try to algorithms, you''re going to also try
    to algorithms, you''re going to also try to

    learn how to improve upon them and how learn how to improve upon them and how
    learn how to improve upon them and how

    to conceptually extend them to discrete to conceptually extend them to discrete
    to conceptually extend them to discrete

    data like text. Uh, and finally, you''re data like text. Uh, and finally, you''re
    data like text. Uh, and finally, you''re

    going to be able to demonstrate how you going to be able to demonstrate how you
    going to be able to demonstrate how you

    think and what what what you did in the think and what what what you did in the
    think and what what what you did in the

    in in this class. Okay, cool. But like the first question Okay, cool. But like
    the first question

    that we probably need to answer is how that we probably need to answer is how
    that we probably need to answer is how

    to train like to train like to train like

    all right in order to answer how to all right in order to answer how to all right
    in order to answer how to

    train a good image generation model you train a good image generation model you
    train a good image generation model you

    probably need to first answer what is a'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 4
  start_sec: 246.949
  end_sec: 292.0
  text: 'probably need to first answer what is a probably need to first answer what
    is a

    good generation uh image generation good generation uh image generation good generation
    uh image generation

    model right so you guys probably already model right so you guys probably already
    model right so you guys probably already

    seen this image before. This is our seen this image before. This is our seen this
    image before. This is our

    class poster. uh but basically class poster. uh but basically class poster. uh
    but basically

    uh what makes a good what makes the uh what makes a good what makes the uh what
    makes a good what makes the

    image generation model good is depend image generation model good is depend image
    generation model good is depend

    depending on the following three depending on the following three depending on
    the following three

    aspects. Uh so the first one is what we aspects. Uh so the first one is what we
    aspects. Uh so the first one is what we

    call fidelity or you can sort of call fidelity or you can sort of call fidelity
    or you can sort of

    understand as like how faithful is the understand as like how faithful is the
    understand as like how faithful is the

    gen images to the real images. So how gen images to the real images. So how gen
    images to the real images. So how

    how real do they look? Um so this boils how real do they look? Um so this boils
    how real do they look? Um so this boils

    down to the questions like do the down to the questions like do the down to the
    questions like do the

    generated people have six fingers? uh if generated people have six fingers? uh
    if generated people have six fingers? uh if

    they do, they probably don''t look as they do, they probably don''t look as they
    do, they probably don''t look as

    real as they could be. And uh are these real as they could be. And uh are these
    real as they could be. And uh are these

    images have like weird colors or are images have like weird colors or are images
    have like weird colors or are

    they like have a lot of like weird they like have a lot of like weird'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 5
  start_sec: 292.0
  end_sec: 334.07
  text: 'they like have a lot of like weird

    artifacts? Um so you probably don''t artifacts? Um so you probably don''t artifacts?
    Um so you probably don''t

    really understand what what weird really understand what what weird really understand
    what what weird

    artifact means, but trust me, when you artifact means, but trust me, when you
    artifact means, but trust me, when you

    do your first homework, you''re going to do your first homework, you''re going
    to do your first homework, you''re going to

    see a lot of them. Uh some of them are see a lot of them. Uh some of them are
    see a lot of them. Uh some of them are

    just like they look like they come from just like they look like they come from
    just like they look like they come from

    hell basically. But um yeah, so the hell basically. But um yeah, so the hell basically.
    But um yeah, so the

    first thing we want to do is to maximize first thing we want to do is to maximize
    first thing we want to do is to maximize

    the fidelity or like how real these the fidelity or like how real these the fidelity
    or like how real these

    images look. The second uh aspect that images look. The second uh aspect that
    images look. The second uh aspect that

    we''re trying to tackle is the we''re trying to tackle is the we''re trying to
    tackle is the

    controllability and this is the thing controllability and this is the thing controllability
    and this is the thing

    that sort of like enables all those that sort of like enables all those that sort
    of like enables all those

    memes. Uh so basically just like can I memes. Uh so basically just like can I
    memes. Uh so basically just like can I

    control what I generate in whatever way control what I generate in whatever way
    control what I generate in whatever way

    that I want. So for example, can I use that I want. So for example, can I use
    that I want. So for example, can I use

    text to describe what I want to generate text to describe what I want to generate
    text to describe what I want to generate

    or can I use another image to you know'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 6
  start_sec: 334.07
  end_sec: 369.039
  text: 'or can I use another image to you know or can I use another image to you
    know

    to specify what I want to generate? For to specify what I want to generate? For
    to specify what I want to generate? For

    example, can I edit an existing image example, can I edit an existing image example,
    can I edit an existing image

    and uh can I generate something that is and uh can I generate something that is
    and uh can I generate something that is

    like completely imaginary, right? Like like completely imaginary, right? Like
    like completely imaginary, right? Like

    can I generate a cat playing basketball can I generate a cat playing basketball
    can I generate a cat playing basketball

    or like a cat playing violins and stuff? or like a cat playing violins and stuff?
    or like a cat playing violins and stuff?

    Uh and can I personalize this model? For Uh and can I personalize this model?
    For Uh and can I personalize this model? For

    example, like I want to generate my cat, example, like I want to generate my cat,
    example, like I want to generate my cat,

    not just any cat. I want to generate not just any cat. I want to generate not
    just any cat. I want to generate

    this one specific cat. Can I do that? this one specific cat. Can I do that? this
    one specific cat. Can I do that?

    And also like can this per can my image And also like can this per can my image
    And also like can this per can my image

    generation model to interact with other generation model to interact with other
    generation model to interact with other

    models? Um so for example like you know models? Um so for example like you know
    models? Um so for example like you know

    can I interact with like a VLM or like a can I interact with like a VLM or like
    a can I interact with like a VLM or like a

    LM or stuff like that or like a reward LM or stuff like that or like a reward
    LM or stuff like that or like a reward

    model. Can we do that? Um so that''s the model. Can we do that? Um so that''s
    the'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 7
  start_sec: 369.039
  end_sec: 405.759
  text: 'model. Can we do that? Um so that''s the

    second aspect. And then the third aspect second aspect. And then the third aspect
    second aspect. And then the third aspect

    is basically how fast is the generation is basically how fast is the generation
    is basically how fast is the generation

    right? So you probably wouldn''t want to right? So you probably wouldn''t want
    to right? So you probably wouldn''t want to

    like wait for like half an hour for an like wait for like half an hour for an
    like wait for like half an hour for an

    image to generate because that''s just image to generate because that''s just
    image to generate because that''s just

    like not practical anymore. Um so like not practical anymore. Um so like not practical
    anymore. Um so

    basically in order to speed up the basically in order to speed up the basically
    in order to speed up the

    generation a couple of uh questions that generation a couple of uh questions that
    generation a couple of uh questions that

    we need to answer basically is that is we need to answer basically is that is
    we need to answer basically is that is

    it possible to speed up the generation it possible to speed up the generation
    it possible to speed up the generation

    without without without

    degrading the the the quality? Is it degrading the the the quality? Is it degrading
    the the the quality? Is it

    possible to speed it up and improve the possible to speed it up and improve the
    possible to speed it up and improve the

    quality at the same time? That would be quality at the same time? That would be
    quality at the same time? That would be

    huge, right? And uh do I need to do huge, right? And uh do I need to do huge,
    right? And uh do I need to do

    extra training to speed it up or can I extra training to speed it up or can I
    extra training to speed it up or can I

    just do it without training? uh and can just do it without training? uh and can
    just do it without training? uh and can

    I reduce war clock time with the same I reduce war clock time with the same'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 8
  start_sec: 405.759
  end_sec: 451.189
  text: 'I reduce war clock time with the same

    amount uh same number of network amount uh same number of network amount uh same
    number of network

    evaluation which means that like you evaluation which means that like you evaluation
    which means that like you

    have the same number of for pass but have the same number of for pass but have
    the same number of for pass but

    somehow the total time that you actually somehow the total time that you actually
    somehow the total time that you actually

    need is uh like smaller uh or can I just need is uh like smaller uh or can I just
    need is uh like smaller uh or can I just

    reduce a wall clock time and the number reduce a wall clock time and the number
    reduce a wall clock time and the number

    of um uh and the number of evaluation at of um uh and the number of evaluation
    at of um uh and the number of evaluation at

    the same time can we do that so we''re the same time can we do that so we''re
    the same time can we do that so we''re

    going to be able to hopefully answer all going to be able to hopefully answer
    all going to be able to hopefully answer all

    these questions uh after we learn in these questions uh after we learn in these
    questions uh after we learn in

    this class all right so uh basic this class all right so uh basic this class all
    right so uh basic

    Basically, the recommended Basically, the recommended Basically, the recommended

    way to learn in this class is just to way to learn in this class is just to way
    to learn in this class is just to

    try to imagine like you''re playing an try to imagine like you''re playing an
    try to imagine like you''re playing an

    RPG game. All right? And uh basically RPG game. All right? And uh basically RPG
    game. All right? And uh basically

    what happens usually in an RPG game is what happens usually in an RPG game is
    what happens usually in an RPG game is

    that you first start at some like that you first start at some like that you first
    start at some like

    beginnings village and where you you you'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 9
  start_sec: 451.189
  end_sec: 487.35
  text: 'beginnings village and where you you you beginnings village and where you
    you you

    get to like fail pretty fast and safely get to like fail pretty fast and safely
    get to like fail pretty fast and safely

    and then you you can learn all the and then you you can learn all the and then
    you you can learn all the

    basics. Uh, and then you sort of after basics. Uh, and then you sort of after
    basics. Uh, and then you sort of after

    before you you leave the village like before you you leave the village like before
    you you leave the village like

    some master be like, "Uh, what what what some master be like, "Uh, what what what
    some master be like, "Uh, what what what

    do you want to do in your life?" And do you want to do in your life?" And do you
    want to do in your life?" And

    then you be like, "I don''t know. I want then you be like, "I don''t know. I want
    then you be like, "I don''t know. I want

    to be the best like Pokemon trainer or to be the best like Pokemon trainer or
    to be the best like Pokemon trainer or

    something." And and and then and before something." And and and then and before
    something." And and and then and before

    you but but before you do that, you you but but before you do that, you you but
    but before you do that, you

    you''re going to be able to choose what you''re going to be able to choose what
    you''re going to be able to choose what

    path that you want to specialize on. Uh, path that you want to specialize on.
    Uh, path that you want to specialize on. Uh,

    and then after you leave the village, and then after you leave the village, and
    then after you leave the village,

    you are going to be like during your you are going to be like during your you
    are going to be like during your

    exploration of the world, you''re going exploration of the world, you''re going
    exploration of the world, you''re going

    to be fighting some like multiple small to be fighting some like multiple small
    to be fighting some like multiple small

    bosses throughout the way. And uh, these'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 10
  start_sec: 487.35
  end_sec: 532.47
  text: 'bosses throughout the way. And uh, these bosses throughout the way. And uh,
    these

    ones are not going to kill you and ones are not going to kill you and ones are
    not going to kill you and

    they''re just going to basically help you they''re just going to basically help
    you they''re just going to basically help you

    to improve your skills. And finally, to improve your skills. And finally, to improve
    your skills. And finally,

    after everything we have done, after everything we have done, after everything
    we have done,

    are we stuck again? Uh, we are not. are we stuck again? Uh, we are not. are we
    stuck again? Uh, we are not.

    Okay. uh you''re you''re going to be able Okay. uh you''re you''re going to be
    able Okay. uh you''re you''re going to be able

    to defeat the final boss and obtain the to defeat the final boss and obtain the
    to defeat the final boss and obtain the

    holy grail. All right. Uh so for those holy grail. All right. Uh so for those
    holy grail. All right. Uh so for those

    of you who don''t know, all of these like of you who don''t know, all of these
    like of you who don''t know, all of these like

    uh game uh like uh uh screenshot come uh game uh like uh uh screenshot come uh
    game uh like uh uh screenshot come

    from the game Seiko, the best game of from the game Seiko, the best game of from
    the game Seiko, the best game of

    all time. All right. Uh so all time. All right. Uh so all time. All right. Uh
    so

    uh okay. So basically we designed a uh okay. So basically we designed a uh okay.
    So basically we designed a

    homework to simulate this sort of uh homework to simulate this sort of uh homework
    to simulate this sort of uh

    experience. Uh so the first two homework experience. Uh so the first two homework
    experience. Uh so the first two homework

    is going to be your beginner''s village is going to be your beginner''s village
    is going to be your beginner''s village

    where you get to like just build your where you get to like just build your where
    you get to like just build your

    environment try to get yourself familiar'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 11
  start_sec: 532.47
  end_sec: 582.55
  text: 'environment try to get yourself familiar environment try to get yourself
    familiar

    with GPU training and also just build with GPU training and also just build with
    GPU training and also just build

    two maybe three two and a half let''s two maybe three two and a half let''s two
    maybe three two and a half let''s

    just say uh foundational algorithms in just say uh foundational algorithms in
    just say uh foundational algorithms in

    the first uh two homeworks and at the the first uh two homeworks and at the the
    first uh two homeworks and at the

    end of the second homework you should be end of the second homework you should
    be end of the second homework you should be

    able to decide like which path like able to decide like which path like able to
    decide like which path like

    which aspect of the image generation do which aspect of the image generation do
    which aspect of the image generation do

    you want to focus on and then the third you want to focus on and then the third
    you want to focus on and then the third

    homework you''re going uh uh like homework you''re going uh uh like homework you''re
    going uh uh like

    basically just implement one baseline basically just implement one baseline basically
    just implement one baseline

    that you choose uh for this specific that you choose uh for this specific that
    you choose uh for this specific

    aspect and then in the fourth homework aspect and then in the fourth homework
    aspect and then in the fourth homework

    you''re going to try to improve upon the you''re going to try to improve upon
    the you''re going to try to improve upon the

    baseline that you choose and hopefully baseline that you choose and hopefully
    baseline that you choose and hopefully

    you''re going to be able to beat it. All you''re going to be able to beat it.
    All you''re going to be able to beat it. All

    right, right, right,

    cool. Uh so in terms of grading these cool. Uh so in terms of grading these cool.
    Uh so in terms of grading these

    are the uh percentage uh ratio. are the uh percentage uh ratio. are the uh percentage
    uh ratio.

    Okay. And uh at the end of the class uh'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 12
  start_sec: 582.55
  end_sec: 619.12
  text: 'Okay. And uh at the end of the class uh Okay. And uh at the end of the class
    uh

    which is the last week uh of class, it''s which is the last week uh of class,
    it''s which is the last week uh of class, it''s

    like last week of February, uh we''re like last week of February, uh we''re like
    last week of February, uh we''re

    going to have two poster sessions in going to have two poster sessions in going
    to have two poster sessions in

    class for everyone to showcase their class for everyone to showcase their class
    for everyone to showcase their

    work. Still trying to figure out if this work. Still trying to figure out if this
    work. Still trying to figure out if this

    is a large enough space for everyone to is a large enough space for everyone to
    is a large enough space for everyone to

    do a poster. Hopefully it is. Um but do a poster. Hopefully it is. Um but do a
    poster. Hopefully it is. Um but

    anyway, the point is uh basically you anyway, the point is uh basically you anyway,
    the point is uh basically you

    need to do three things. The first thing need to do three things. The first thing
    need to do three things. The first thing

    is you need to submit your poster PDF is you need to submit your poster PDF is
    you need to submit your poster PDF

    the day before the first uh poster the day before the first uh poster the day
    before the first uh poster

    session so that everyone is like so that session so that everyone is like so that
    session so that everyone is like so that

    it''s fair for everyone like and you know it''s fair for everyone like and you
    know it''s fair for everyone like and you know

    you need to finish it up uh by the same you need to finish it up uh by the same
    you need to finish it up uh by the same

    deadline and then uh the second thing is deadline and then uh the second thing
    is deadline and then uh the second thing is

    to actually present your poster in class to actually present your poster in class'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 13
  start_sec: 619.12
  end_sec: 658.48
  text: 'to actually present your poster in class

    you know tell your classmate what you you know tell your classmate what you you
    know tell your classmate what you

    did and then the third thing is you did and then the third thing is you did and
    then the third thing is you

    actually need to attend the other uh actually need to attend the other uh actually
    need to attend the other uh

    poster session so that you can check out poster session so that you can check
    out poster session so that you can check out

    other people''s work uh and then at the other people''s work uh and then at the
    other people''s work uh and then at the

    end of the uh I guess we we we should end of the uh I guess we we we should end
    of the uh I guess we we we should

    probably do it in each uh probably do it in each uh probably do it in each uh

    poster session, but basically during the poster session, but basically during
    the poster session, but basically during the

    poster session uh we''re going to be poster session uh we''re going to be poster
    session uh we''re going to be

    conducting a poll uh where everyone get conducting a poll uh where everyone get
    conducting a poll uh where everyone get

    to vote for their favorite posters and to vote for their favorite posters and
    to vote for their favorite posters and

    the best poster for each path, each the best poster for each path, each the best
    poster for each path, each

    aspect is going to receive a small aspect is going to receive a small aspect is
    going to receive a small

    reward. I''m uh I''m still thinking about reward. I''m uh I''m still thinking
    about reward. I''m uh I''m still thinking about

    what kind of things to get you guys, but what kind of things to get you guys,
    but what kind of things to get you guys, but

    it shall be fun. It shall be fun. All it shall be fun. It shall be fun. All it
    shall be fun. It shall be fun. All

    right. Uh so a couple of things to right. Uh so a couple of things to'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 14
  start_sec: 658.48
  end_sec: 713.03
  text: 'right. Uh so a couple of things to

    remind you guys is that uh this class is remind you guys is that uh this class
    is remind you guys is that uh this class is

    completely AI friendly and open completely AI friendly and open completely AI
    friendly and open

    everything. Uh so basically what it everything. Uh so basically what it everything.
    Uh so basically what it

    means is that you can use any and all AI means is that you can use any and all
    AI means is that you can use any and all AI

    tools that you want whether it''s like tools that you want whether it''s like
    tools that you want whether it''s like

    clock code cursor codeex chat gpt uh I clock code cursor codeex chat gpt uh I
    clock code cursor codeex chat gpt uh I

    don''t know deepseeek anything you can don''t know deepseeek anything you can
    don''t know deepseeek anything you can

    you can use anything everything that you you can use anything everything that
    you you can use anything everything that you

    want you can refer to any open source want you can refer to any open source want
    you can refer to any open source

    code because AI are trained on these code because AI are trained on these code
    because AI are trained on these

    things anyway uh you can also use any things anyway uh you can also use any things
    anyway uh you can also use any

    pre-trained models although if you pre-trained models although if you pre-trained
    models although if you

    directly directly directly

    use it I''m not sure the your homework use it I''m not sure the your homework
    use it I''m not sure the your homework

    results are going to be that good. Uh results are going to be that good. Uh results
    are going to be that good. Uh

    and and and

    the and any uh research papers, books or the and any uh research papers, books
    or the and any uh research papers, books or

    tutorials that you want to refer to and tutorials that you want to refer to and
    tutorials that you want to refer to and

    you can also obviously discuss you can also obviously discuss you can also obviously
    discuss

    everything with other everything with other everything with other

    people. However, uh because we''re so'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 15
  start_sec: 713.03
  end_sec: 753.829
  text: 'people. However, uh because we''re so people. However, uh because we''re
    so

    flexible on our you know just like open flexible on our you know just like open
    flexible on our you know just like open

    source uh policies, you should be able source uh policies, you should be able
    source uh policies, you should be able

    to complete everything on your own. I to complete everything on your own. I to
    complete everything on your own. I

    shall hope this is the case. It''s I shall hope this is the case. It''s I shall
    hope this is the case. It''s I

    don''t think it should be that difficult don''t think it should be that difficult
    don''t think it should be that difficult

    uh especially if you have you know AI to uh especially if you have you know AI
    to uh especially if you have you know AI to

    help you. Uh but regardless you should help you. Uh but regardless you should
    help you. Uh but regardless you should

    site everything that you use in site everything that you use in site everything
    that you use in

    including what AI tools that you use. including what AI tools that you use. including
    what AI tools that you use.

    Uh and please do not copy from other Uh and please do not copy from other Uh and
    please do not copy from other

    people. Uh just like because you can people. Uh just like because you can people.
    Uh just like because you can

    already copy from AI and AI can do already copy from AI and AI can do already
    copy from AI and AI can do

    things for you. Just don''t copy from things for you. Just don''t copy from things
    for you. Just don''t copy from

    other people. Uh and do not claim other other people. Uh and do not claim other
    other people. Uh and do not claim other

    people''s work as yours. So if you refer people''s work as yours. So if you refer
    people''s work as yours. So if you refer

    to something just site it just like to something just site it just like to something
    just site it just like

    clearly indicate it. It''s fine. just clearly indicate it. It''s fine. just clearly
    indicate it. It''s fine. just

    like it''s totally fine and yeah just in'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 16
  start_sec: 753.829
  end_sec: 800.639
  text: 'like it''s totally fine and yeah just in like it''s totally fine and yeah
    just in

    general do not plagiarize. It''s you know general do not plagiarize. It''s you
    know general do not plagiarize. It''s you know

    just just do your proper citation. Okay. just just do your proper citation. Okay.
    just just do your proper citation. Okay.

    Uh besides AI there are a couple of Uh besides AI there are a couple of Uh besides
    AI there are a couple of

    humans that can help you uh throughout humans that can help you uh throughout
    humans that can help you uh throughout

    this journey. So the person with the this journey. So the person with the this
    journey. So the person with the

    blue hair in case you do not notice that blue hair in case you do not notice that
    blue hair in case you do not notice that

    is me. Um and these are two of my is me. Um and these are two of my is me. Um
    and these are two of my

    adviserss. Um so they''re very supportive adviserss. Um so they''re very supportive
    adviserss. Um so they''re very supportive

    on us just being on this journey. Uh and on us just being on this journey. Uh
    and on us just being on this journey. Uh and

    then Michelle is the education then Michelle is the education then Michelle is
    the education

    associate. Uh, so she''s going to associate. Uh, so she''s going to associate.
    Uh, so she''s going to

    probably probably probably

    provide support anything outside of the provide support anything outside of the
    provide support anything outside of the

    class material. Um, so yeah, feel free class material. Um, so yeah, feel free
    class material. Um, so yeah, feel free

    to reach out to her if you need any like to reach out to her if you need any like
    to reach out to her if you need any like

    accommodations and stuff. And we also accommodations and stuff. And we also accommodations
    and stuff. And we also

    today we learned that we recruited two today we learned that we recruited two
    today we learned that we recruited two

    TAs. Uh, this is amazing. Uh, but TAs. Uh, this is amazing. Uh, but TAs. Uh, this
    is amazing. Uh, but

    basically um basically um'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 17
  start_sec: 800.639
  end_sec: 840.639
  text: 'basically um

    so uh myself and the TAs are going to so uh myself and the TAs are going to so
    uh myself and the TAs are going to

    start hosting office hours um next week. start hosting office hours um next week.
    start hosting office hours um next week.

    Um but uh yeah and the the the time and Um but uh yeah and the the the time and
    Um but uh yeah and the the the time and

    location is going to be announced on the location is going to be announced on
    the location is going to be announced on the

    website and also on discord which we''re website and also on discord which we''re
    website and also on discord which we''re

    going to talk about later. Uh but in going to talk about later. Uh but in going
    to talk about later. Uh but in

    general TAS are your peers because this general TAS are your peers because this
    general TAS are your peers because this

    is this class is like this is the first is this class is like this is the first
    is this class is like this is the first

    time we''re doing a diffusion flow time we''re doing a diffusion flow time we''re
    doing a diffusion flow

    matching class at CMU. No one has taken matching class at CMU. No one has taken
    matching class at CMU. No one has taken

    this class before. So obviously there''s this class before. So obviously there''s
    this class before. So obviously there''s

    like a you know there''s only so much you like a you know there''s only so much
    you like a you know there''s only so much you

    can do. Uh so a TAS are your peers can do. Uh so a TAS are your peers can do.
    Uh so a TAS are your peers

    they''re also learning with you guys and they''re also learning with you guys
    and they''re also learning with you guys and

    so basically you know just uh just keep so basically you know just uh just keep
    so basically you know just uh just keep

    that in mind. But they are they that in mind. But they are they that in mind.
    But they are they

    they do know um you know they they have they do know um you know they they have'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 18
  start_sec: 840.639
  end_sec: 884.24
  text: 'they do know um you know they they have

    done research in terms of well Douglas done research in terms of well Douglas
    done research in terms of well Douglas

    has done research in terms of flow has done research in terms of flow has done
    research in terms of flow

    matching and then uh Chris has done matching and then uh Chris has done matching
    and then uh Chris has done

    research uh in terms of diffusion research uh in terms of diffusion research uh
    in terms of diffusion

    models. So like just feel free to ask models. So like just feel free to ask models.
    So like just feel free to ask

    them any questions and uh but yeah but them any questions and uh but yeah but
    them any questions and uh but yeah but

    try to also figure things out on your try to also figure things out on your try
    to also figure things out on your

    own and also ask AI about it. Cool. own and also ask AI about it. Cool. own and
    also ask AI about it. Cool.

    All right. Uh so basically uh All right. Uh so basically uh All right. Uh so basically
    uh

    uh the idea here is that like I''m going uh the idea here is that like I''m going
    uh the idea here is that like I''m going

    to be so so like how we''re going to to be so so like how we''re going to to be
    so so like how we''re going to

    learn in this class is that the lectures learn in this class is that the lectures
    learn in this class is that the lectures

    and I is going to be providing uh and I is going to be providing uh and I is going
    to be providing uh

    providing some intuition and math and providing some intuition and math and providing
    some intuition and math and

    some pointers to the the resources that some pointers to the the resources that
    some pointers to the the resources that

    you can use and you and your AI and you can use and you and your AI and you can
    use and you and your AI and

    probably your classmate are going to probably your classmate are going to'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 19
  start_sec: 884.24
  end_sec: 927.99
  text: 'probably your classmate are going to

    figure like a lot of things out on your figure like a lot of things out on your
    figure like a lot of things out on your

    own through ex own through ex own through ex

    experiments and homework uh experiments and homework uh experiments and homework
    uh

    implementations. implementations. implementations.

    Uh and uh that being said because this Uh and uh that being said because this
    Uh and uh that being said because this

    is like a really AI friendly class and a is like a really AI friendly class and
    a is like a really AI friendly class and a

    lot of people are actually you know lot of people are actually you know lot of
    people are actually you know

    having some concern about whether or not having some concern about whether or
    not having some concern about whether or not

    this kind of like this new type of like this kind of like this new type of like
    this kind of like this new type of like

    classroom setting is going to work. Uh classroom setting is going to work. Uh
    classroom setting is going to work. Uh

    so to make sure that everything are so to make sure that everything are so to
    make sure that everything are

    going to work uh we''re going to be going to work uh we''re going to be going
    to work uh we''re going to be

    benchmarking learning in a more benchmarking learning in a more benchmarking learning
    in a more

    traditional way a little bit. Uh so traditional way a little bit. Uh so traditional
    way a little bit. Uh so

    that''s why 15% of the grade is going to that''s why 15% of the grade is going
    to that''s why 15% of the grade is going to

    go to uh an in-class quiz. Uh so this is go to uh an in-class quiz. Uh so this
    is go to uh an in-class quiz. Uh so this is

    like the only part of the class where like the only part of the class where like
    the only part of the class where

    you are not allowed to use anything. Uh you are not allowed to use anything. Uh
    you are not allowed to use anything. Uh

    by anything I mean you''re not allowed to'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 20
  start_sec: 927.99
  end_sec: 967.35
  text: 'by anything I mean you''re not allowed to by anything I mean you''re not
    allowed to

    use your laptop at all. So just going to use your laptop at all. So just going
    to use your laptop at all. So just going to

    be pen and pencil uh pencil and paper I be pen and pencil uh pencil and paper
    I be pen and pencil uh pencil and paper I

    guess. Uh you just sit in class for 10 guess. Uh you just sit in class for 10
    guess. Uh you just sit in class for 10

    minutes and then just like do some uh do minutes and then just like do some uh
    do minutes and then just like do some uh do

    some quizzes like like we did when when some quizzes like like we did when when
    some quizzes like like we did when when

    I was a kid. Okay. Um, but uh that being I was a kid. Okay. Um, but uh that being
    I was a kid. Okay. Um, but uh that being

    said, these quizzes are meant to serve said, these quizzes are meant to serve
    said, these quizzes are meant to serve

    as uh sanity checks for learning. So, as uh sanity checks for learning. So, as
    uh sanity checks for learning. So,

    they''re just going to be super easy. Uh, they''re just going to be super easy.
    Uh, they''re just going to be super easy. Uh,

    you should be able to know how to answer you should be able to know how to answer
    you should be able to know how to answer

    all of these if you you know, either pay all of these if you you know, either
    pay all of these if you you know, either pay

    attention to class or, you know, you attention to class or, you know, you attention
    to class or, you know, you

    you''ve done your homework or, you know, you''ve done your homework or, you know,
    you''ve done your homework or, you know,

    you''ve read the tutorials that I sent you''ve read the tutorials that I sent
    you''ve read the tutorials that I sent

    that that in the in the class uh that that in the in the class uh that that in
    the in the class uh

    website. Basically, they''re just like'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 21
  start_sec: 967.35
  end_sec: 1014.72
  text: 'website. Basically, they''re just like website. Basically, they''re just
    like

    easy conceptual questions. Uh, and they easy conceptual questions. Uh, and they
    easy conceptual questions. Uh, and they

    should not heavily impact your final should not heavily impact your final should
    not heavily impact your final

    grade because you can drop two lowest grade because you can drop two lowest grade
    because you can drop two lowest

    quizzes. Um, so yeah, but like if you''re quizzes. Um, so yeah, but like if you''re
    quizzes. Um, so yeah, but like if you''re

    not doing well on one of the quiz, that not doing well on one of the quiz, that
    not doing well on one of the quiz, that

    doesn''t mean you''re a bad student. It doesn''t mean you''re a bad student. It
    doesn''t mean you''re a bad student. It

    literally just means that you probably literally just means that you probably
    literally just means that you probably

    need to pay more attention on that part need to pay more attention on that part
    need to pay more attention on that part

    of the class and that''s it. Okay, cool. of the class and that''s it. Okay, cool.
    of the class and that''s it. Okay, cool.

    All right. Besides everything, we are All right. Besides everything, we are All
    right. Besides everything, we are

    also going to be having some extra also going to be having some extra also going
    to be having some extra

    credit opportunities. Uh basically this credit opportunities. Uh basically this
    credit opportunities. Uh basically this

    is like the first class that we''re going is like the first class that we''re
    going is like the first class that we''re going

    to try to do what we do here by allowing to try to do what we do here by allowing
    to try to do what we do here by allowing

    clock code essentially. Uh so uh clock code essentially. Uh so uh clock code essentially.
    Uh so uh

    throughout the class we''re going to be throughout the class we''re going to be
    throughout the class we''re going to be

    releasing two optional uh surveys and releasing two optional uh surveys and releasing
    two optional uh surveys and

    interview in person interview oneonone interview in person interview oneonone
    interview in person interview oneonone

    with me uh to collect feedback on your with me uh to collect feedback on your'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 22
  start_sec: 1014.72
  end_sec: 1051.919
  text: 'with me uh to collect feedback on your

    learning experience in this class. And learning experience in this class. And
    learning experience in this class. And

    uh yeah basically it''s just going to be uh yeah basically it''s just going to
    be uh yeah basically it''s just going to be

    like I ask you do you think you''re like I ask you do you think you''re like I
    ask you do you think you''re

    learning anything or do you think you learning anything or do you think you learning
    anything or do you think you

    learn nothing? Um that that''s pretty learn nothing? Um that that''s pretty learn
    nothing? Um that that''s pretty

    much that. Um yeah and uh yeah but extra much that. Um yeah and uh yeah but extra
    much that. Um yeah and uh yeah but extra

    credit will be applied upon completion credit will be applied upon completion
    credit will be applied upon completion

    in both cases. All right cool. Uh so a in both cases. All right cool. Uh so a
    in both cases. All right cool. Uh so a

    little bit of overview of what we''re little bit of overview of what we''re little
    bit of overview of what we''re

    going to be learning like specifically going to be learning like specifically
    going to be learning like specifically

    uh topic uh topic uh topic

    wise. Uh so in the first two weeks we''re wise. Uh so in the first two weeks we''re
    wise. Uh so in the first two weeks we''re

    going to be just like covering the going to be just like covering the going to
    be just like covering the

    basics and the foundational algorithm. basics and the foundational algorithm.
    basics and the foundational algorithm.

    Basically just we''re going to be talking Basically just we''re going to be talking
    Basically just we''re going to be talking

    about what is diffusion and what is flow about what is diffusion and what is flow
    about what is diffusion and what is flow

    matching in the first two weeks and the matching in the first two weeks and the
    matching in the first two weeks and the

    uh third and fourth week we''re going to uh third and fourth week we''re going
    to uh third and fourth week we''re going to

    talk about like how people have been talk about like how people have been'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 23
  start_sec: 1051.919
  end_sec: 1097.11
  text: 'talk about like how people have been

    trying to improve upon those uh basic trying to improve upon those uh basic trying
    to improve upon those uh basic

    algorithms throughout the years. Uh and algorithms throughout the years. Uh and
    algorithms throughout the years. Uh and

    then the fifth week we''re going to be then the fifth week we''re going to be
    then the fifth week we''re going to be

    talking about uh currently like what we talking about uh currently like what we
    talking about uh currently like what we

    think what people do uh to develop sot think what people do uh to develop sot
    think what people do uh to develop sot

    models and also how what people are models and also how what people are models
    and also how what people are

    using in the industry and specifically using in the industry and specifically
    using in the industry and specifically

    in the fifth week we''re going to have a in the fifth week we''re going to have
    a in the fifth week we''re going to have a

    guest lecture from uh Luma AI. Uh so guest lecture from uh Luma AI. Uh so guest
    lecture from uh Luma AI. Uh so

    this is a company that did the the the this is a company that did the the the
    this is a company that did the the the

    the dream machine. The dreaming machine. the dream machine. The dreaming machine.
    the dream machine. The dreaming machine.

    I guess it''s just like the first uh you I guess it''s just like the first uh
    you I guess it''s just like the first uh you

    know AI uh video generation model that know AI uh video generation model that
    know AI uh video generation model that

    just like make your meme move if you just like make your meme move if you just
    like make your meme move if you

    guys remember from like 2024. It''s guys remember from like 2024. It''s guys remember
    from like 2024. It''s

    pretty cool. But we''re going to have a pretty cool. But we''re going to have
    a pretty cool. But we''re going to have a

    guest lecture from that company. Uh and guest lecture from that company. Uh and
    guest lecture from that company. Uh and

    then week six is going to be we''re going'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 24
  start_sec: 1097.11
  end_sec: 1146.63
  text: 'then week six is going to be we''re going then week six is going to be we''re
    going

    to be talking about probably a lot of to be talking about probably a lot of to
    be talking about probably a lot of

    you guys are going to be interested in you guys are going to be interested in
    you guys are going to be interested in

    this. It''s going to be uh you know this. It''s going to be uh you know this.
    It''s going to be uh you know

    discrete diffusion discrete flow discrete diffusion discrete flow discrete diffusion
    discrete flow

    matching. So specifically like mass matching. So specifically like mass matching.
    So specifically like mass

    diffusion models and like uh edit flow diffusion models and like uh edit flow
    diffusion models and like uh edit flow

    which is like a new type of um text which is like a new type of um text which
    is like a new type of um text

    generation model and then seven is just generation model and then seven is just
    generation model and then seven is just

    going to be your poster session. Cool. going to be your poster session. Cool.
    going to be your poster session. Cool.

    All right. So a couple of uh you know helpful links here. Uh the class website
    helpful links here. Uh the class website

    is your one-stop shop for everything is your one-stop shop for everything is your
    one-stop shop for everything

    basically. You should just like check it basically. You should just like check
    it basically. You should just like check it

    uh like regularly. Uh it has literally uh like regularly. Uh it has literally
    uh like regularly. Uh it has literally

    everything on it. We I I literally po everything on it. We I I literally po everything
    on it. We I I literally po

    post everything on it including your post everything on it including your post
    everything on it including your

    lecture slide, homework link, uh you lecture slide, homework link, uh you lecture
    slide, homework link, uh you

    know, papers you should read, any know, papers you should read, any know, papers
    you should read, any

    announcement. I''m just like I''m going to announcement. I''m just like I''m going
    to announcement. I''m just like I''m going to

    post it on there. Um and uh'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 25
  start_sec: 1146.63
  end_sec: 1196.39
  text: 'post it on there. Um and uh post it on there. Um and uh

    the gray scope, which I have not add the gray scope, which I have not add the
    gray scope, which I have not add

    anyone to, by the way, so don''t panic if anyone to, by the way, so don''t panic
    if anyone to, by the way, so don''t panic if

    you uh if you don''t see your grade scope you uh if you don''t see your grade
    scope you uh if you don''t see your grade scope

    invitation. But basically, we''re going invitation. But basically, we''re going
    invitation. But basically, we''re going

    to be using grayscope to keep track of to be using grayscope to keep track of
    to be using grayscope to keep track of

    all the grades. All right? And also all the grades. All right? And also all the
    grades. All right? And also

    submit homework. Cool. Very important submit homework. Cool. Very important submit
    homework. Cool. Very important

    thing. Discord server. Please join your thing. Discord server. Please join your
    thing. Discord server. Please join your

    Discord server. Discord server. Discord server.

    All right. Cool. But basically this All right. Cool. But basically this All right.
    Cool. But basically this

    Discord server is your Piaza basically Discord server is your Piaza basically
    Discord server is your Piaza basically

    or this is sort of like a instantaneous or this is sort of like a instantaneous
    or this is sort of like a instantaneous

    Piaza situation like a piaza plus um Piaza situation like a piaza plus um Piaza
    situation like a piaza plus um

    like slack where we kind of just where like slack where we kind of just where
    like slack where we kind of just where

    where we''re going to have like a more uh where we''re going to have like a more
    uh where we''re going to have like a more uh

    immediate communication going and also immediate communication going and also
    immediate communication going and also

    just like it also serves as just regular just like it also serves as just regular
    just like it also serves as just regular

    piaza uh purpose uh where we''re going to piaza uh purpose uh where we''re going
    to piaza uh purpose uh where we''re going to

    have announcement thank you um forum uh'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 26
  start_sec: 1196.39
  end_sec: 1239.6
  text: 'have announcement thank you um forum uh have announcement thank you um forum
    uh

    uh uh discussions you and feel free to uh uh discussions you and feel free to
    uh uh discussions you and feel free to

    share memes. And I''m going to be hosting share memes. And I''m going to be hosting
    share memes. And I''m going to be hosting

    virtual office hours on there too, virtual office hours on there too, virtual
    office hours on there too,

    probably once a week. And uh we''re all probably once a week. And uh we''re all
    probably once a week. And uh we''re all

    we also have the virtual studying room we also have the virtual studying room
    we also have the virtual studying room

    set up so that you guys can just like set up so that you guys can just like set
    up so that you guys can just like

    talk in there. Yeah. So yeah, you may talk in there. Yeah. So yeah, you may talk
    in there. Yeah. So yeah, you may

    ask why do I use why do I choose ask why do I use why do I choose ask why do I
    use why do I choose

    Discord? It''s because Slack, thank you Discord? It''s because Slack, thank you
    Discord? It''s because Slack, thank you

    for your subscription. Uh it''s because for your subscription. Uh it''s because
    for your subscription. Uh it''s because

    uh Slack needs money. So that''s why. All uh Slack needs money. So that''s why.
    All uh Slack needs money. So that''s why. All

    right. right. right.

    Cool. All right. About compute. Uh Cool. All right. About compute. Uh Cool. All
    right. About compute. Uh

    remember how we said ah we are gonna be remember how we said ah we are gonna be
    remember how we said ah we are gonna be

    training models uh using GPUs. Uh let me training models uh using GPUs. Uh let
    me training models uh using GPUs. Uh let me

    actually do a survey now. How many actually do a survey now. How many actually
    do a survey now. How many

    people already have access to GPUs on a people already have access to GPUs on
    a people already have access to GPUs on a

    constant basis? Raise your hand if you constant basis? Raise your hand if you'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 27
  start_sec: 1239.6
  end_sec: 1290.08
  text: 'constant basis? Raise your hand if you

    do. All right. Amazing. All right. Amazing.

    Actually uh a lot of people do. For Actually uh a lot of people do. For Actually
    uh a lot of people do. For

    those of you who don''t um we are super those of you who don''t um we are super
    those of you who don''t um we are super

    grateful for model to sponsor this grateful for model to sponsor this grateful
    for model to sponsor this

    class. Um yeah, but basically model is a class. Um yeah, but basically model is
    a class. Um yeah, but basically model is a

    uh serverless cloud compute company. Um uh serverless cloud compute company. Um
    uh serverless cloud compute company. Um

    so you build everything up on in code. so you build everything up on in code.
    so you build everything up on in code.

    So you don''t need to set up any instance So you don''t need to set up any instance
    So you don''t need to set up any instance

    or like keep it running and stuff like or like keep it running and stuff like
    or like keep it running and stuff like

    that. It''s actually super easy to use. that. It''s actually super easy to use.
    that. It''s actually super easy to use.

    I''ve been using model to test the I''ve been using model to test the I''ve been
    using model to test the

    homework code that I was prototyping. homework code that I was prototyping. homework
    code that I was prototyping.

    It''s really really easy. Uh and but It''s really really easy. Uh and but It''s
    really really easy. Uh and but

    anyway, everyone who registered in this anyway, everyone who registered in this
    anyway, everyone who registered in this

    class will get $500 credit uh for this class will get $500 credit uh for this
    class will get $500 credit uh for this

    class class class

    and uh every user in general in model and uh every user in general in model and
    uh every user in general in model

    will get $30 uh you know credit for will get $30 uh you know credit for will get
    $30 uh you know credit for

    free. Uh so in total you should be able free. Uh so in total you should be able'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 28
  start_sec: 1290.08
  end_sec: 1339.27
  text: 'free. Uh so in total you should be able

    to get around like 280 GP hours on L4DS. to get around like 280 GP hours on L4DS.
    to get around like 280 GP hours on L4DS.

    Um and that should be plenty and should Um and that should be plenty and should
    Um and that should be plenty and should

    be enough for our class. But uh like be enough for our class. But uh like be enough
    for our class. But uh like

    basically if you want to use model uh or basically if you want to use model uh
    or basically if you want to use model uh or

    if like uh the people from the company if like uh the people from the company
    if like uh the people from the company

    is going to give us a guest lecture on is going to give us a guest lecture on
    is going to give us a guest lecture on

    how to use their like uh service this how to use their like uh service this how
    to use their like uh service this

    Friday, same time, same location. So Friday, same time, same location. So Friday,
    same time, same location. So

    5:00 pm this classroom. Uh so feel free 5:00 pm this classroom. Uh so feel free
    5:00 pm this classroom. Uh so feel free

    to join. It''s also going to be on Zoom, to join. It''s also going to be on Zoom,
    to join. It''s also going to be on Zoom,

    but feel free to join in class as well. but feel free to join in class as well.
    but feel free to join in class as well.

    And um just in case that the $500 is not And um just in case that the $500 is
    not And um just in case that the $500 is not

    enough, we all we''re also very grateful enough, we all we''re also very grateful
    enough, we all we''re also very grateful

    for AWS to sponsor our class as well. for AWS to sponsor our class as well. for
    AWS to sponsor our class as well.

    And yeah, so I''m sure everyone know what And yeah, so I''m sure everyone know
    what And yeah, so I''m sure everyone know what

    AWS is, but it''s just like another uh'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 29
  start_sec: 1339.27
  end_sec: 1385.039
  text: 'AWS is, but it''s just like another uh AWS is, but it''s just like another
    uh

    cloud comput service that is very very cloud comput service that is very very
    cloud comput service that is very very

    popular. Um but basically we''re still popular. Um but basically we''re still
    popular. Um but basically we''re still

    finalizing finalizing finalizing

    how much money everyone gets, but how much money everyone gets, but how much money
    everyone gets, but

    hopefully it''s going to be in the range hopefully it''s going to be in the range
    hopefully it''s going to be in the range

    to from $100 to $500ish. Uh and to from $100 to $500ish. Uh and to from $100 to
    $500ish. Uh and

    apparently AWS can also sponsor pizza apparently AWS can also sponsor pizza apparently
    AWS can also sponsor pizza

    party for our uh poster session. So party for our uh poster session. So party
    for our uh poster session. So

    let''s see if that''s uh you know how how let''s see if that''s uh you know how
    how let''s see if that''s uh you know how how

    we''re going to arrange that later. But we''re going to arrange that later. But
    we''re going to arrange that later. But

    yeah, thank you AWS for sponsoring this yeah, thank you AWS for sponsoring this
    yeah, thank you AWS for sponsoring this

    uh class. All right. Uh if you are uh class. All right. Uh if you are uh class.
    All right. Uh if you are

    auditing uh unfortunately uh I can auditing uh unfortunately uh I can auditing
    uh unfortunately uh I can

    cannot give you money. Sorry I cannot cannot give you money. Sorry I cannot cannot
    give you money. Sorry I cannot

    give you GPU. Uh but there are a lot of give you GPU. Uh but there are a lot of
    give you GPU. Uh but there are a lot of

    uh you know freeish uh resources that uh you know freeish uh resources that uh
    you know freeish uh resources that

    you can get. Uh the first thing is if you can get. Uh the first thing is if you
    can get. Uh the first thing is if

    you are a MLDD student or LTI student or you are a MLDD student or LTI student
    or'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 30
  start_sec: 1385.039
  end_sec: 1425.919
  text: 'you are a MLDD student or LTI student or

    probably any SCES student at this point probably any SCES student at this point
    probably any SCES student at this point

    uh you can probably get access to the uh you can probably get access to the uh
    you can probably get access to the

    CMU compute cluster uh Babel I don''t CMU compute cluster uh Babel I don''t CMU
    compute cluster uh Babel I don''t

    think flame is going to be appropriate think flame is going to be appropriate
    think flame is going to be appropriate

    for you know training model for the for you know training model for the for you
    know training model for the

    class but you know just don''t tell class but you know just don''t tell class
    but you know just don''t tell

    Graham I guess uh anyway uh but like you Graham I guess uh anyway uh but like
    you Graham I guess uh anyway uh but like you

    can probably get access to Babel uh by can probably get access to Babel uh by
    can probably get access to Babel uh by

    applying uh and uh you can you can just applying uh and uh you can you can just
    applying uh and uh you can you can just

    use any GP on it and it''s perfectly use any GP on it and it''s perfectly use
    any GP on it and it''s perfectly

    doable. to train models uh to train doable. to train models uh to train doable.
    to train models uh to train

    models for the class on Babel. Uh if you models for the class on Babel. Uh if
    you models for the class on Babel. Uh if you

    are if you''re working for a lab, your are if you''re working for a lab, your
    are if you''re working for a lab, your

    lab probably has GPU as well. H if you lab probably has GPU as well. H if you
    lab probably has GPU as well. H if you

    are not able to get access to Babel or are not able to get access to Babel or
    are not able to get access to Babel or

    any lab clusters, uh then uh I have any lab clusters, uh then uh I have'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 31
  start_sec: 1425.919
  end_sec: 1480.31
  text: 'any lab clusters, uh then uh I have

    listed a bunch of uh freeish and listed a bunch of uh freeish and listed a bunch
    of uh freeish and

    cheapish uh cloud comput service that cheapish uh cloud comput service that cheapish
    uh cloud comput service that

    you can rent. Uh, I think um each you can rent. Uh, I think um each you can rent.
    Uh, I think um each

    homework should probably homework should probably homework should probably

    uh cost you uh cost you uh cost you

    around $30 to $50. Um around $30 to $50. Um around $30 to $50. Um

    um depending on how expensive you want um depending on how expensive you want
    um depending on how expensive you want

    to go. Um but yeah, it should be to go. Um but yeah, it should be to go. Um but
    yeah, it should be

    relatively um it''s it''s not like relatively um it''s it''s not like relatively
    um it''s it''s not like

    completely not doable, but I understand completely not doable, but I understand
    completely not doable, but I understand

    that this is like not a cost that you that this is like not a cost that you that
    this is like not a cost that you

    probably want to spend. you can spend probably want to spend. you can spend probably
    want to spend. you can spend

    $50 on bubble tea or something. It''s $50 on bubble tea or something. It''s $50
    on bubble tea or something. It''s

    better than that. So, like just uh try better than that. So, like just uh try
    better than that. So, like just uh try

    to get free compute first. Okay. All to get free compute first. Okay. All to get
    free compute first. Okay. All

    right. Uh oh, also another thing about right. Uh oh, also another thing about
    right. Uh oh, also another thing about

    compute just in general, uh if you''re compute just in general, uh if you''re
    compute just in general, uh if you''re

    using uh any if you''re like running any using uh any if you''re like running
    any using uh any if you''re like running any

    instance, remember to shut it down when instance, remember to shut it down when
    instance, remember to shut it down when

    you''re not using it. Do not go bankrupt'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 32
  start_sec: 1480.31
  end_sec: 1523.84
  text: 'you''re not using it. Do not go bankrupt you''re not using it. Do not go
    bankrupt

    uh when you''re training models. This is uh when you''re training models. This
    is uh when you''re training models. This is

    not what we want. Okay. not what we want. Okay. not what we want. Okay.

    Uh so speaking of auditing uh basically Uh so speaking of auditing uh basically
    Uh so speaking of auditing uh basically

    what what''s going to happen I know that what what''s going to happen I know that
    what what''s going to happen I know that

    a lot of people are still weight listed a lot of people are still weight listed
    a lot of people are still weight listed

    now. Um yeah so what''s going to happen now. Um yeah so what''s going to happen
    now. Um yeah so what''s going to happen

    from now on is that like as people are from now on is that like as people are
    from now on is that like as people are

    dropping from the class during the first dropping from the class during the first
    dropping from the class during the first

    week we''re going to gradually admit week we''re going to gradually admit week
    we''re going to gradually admit

    students. Thank you Laura for doing that students. Thank you Laura for doing that
    students. Thank you Laura for doing that

    uh from the wait list uh until probably uh from the wait list uh until probably
    uh from the wait list uh until probably

    Friday noonish. So Friday is actually Friday noonish. So Friday is actually Friday
    noonish. So Friday is actually

    the last day that we''re g going to be the last day that we''re g going to be
    the last day that we''re g going to be

    able to add people. Uh so this is also able to add people. Uh so this is also
    able to add people. Uh so this is also

    why uh we''re going to be giving out the why uh we''re going to be giving out
    the why uh we''re going to be giving out the

    model uh credit on Friday when we model uh credit on Friday when we model uh credit
    on Friday when we

    finalize the list of registered student finalize the list of registered student'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 33
  start_sec: 1523.84
  end_sec: 1562.48
  text: 'finalize the list of registered student

    and uh yeah but like whether or not you and uh yeah but like whether or not you
    and uh yeah but like whether or not you

    are going to be able to register please are going to be able to register please
    are going to be able to register please

    join the discord service uh sorry join the discord service uh sorry join the discord
    service uh sorry

    discord server um this is just yeah you discord server um this is just yeah you
    discord server um this is just yeah you

    can just you can just talk you don''t can just you can just talk you don''t can
    just you can just talk you don''t

    need to be registered um and uh but yeah need to be registered um and uh but yeah
    need to be registered um and uh but yeah

    but feel free to just sit in class and but feel free to just sit in class and
    but feel free to just sit in class and

    participate in any way you like. The participate in any way you like. The participate
    in any way you like. The

    only thing that is going to be different only thing that is going to be different
    only thing that is going to be different

    is that I''m not going to be able to give is that I''m not going to be able to
    give is that I''m not going to be able to give

    you money and I''m not going to be able you money and I''m not going to be able
    you money and I''m not going to be able

    to grade your homework. That''s like the to grade your homework. That''s like
    the to grade your homework. That''s like the

    only thing. But feel free to come to only thing. But feel free to come to only
    thing. But feel free to come to

    office hours, sit in class, you know, uh office hours, sit in class, you know,
    uh office hours, sit in class, you know, uh

    chat on Discord, however you like. Okay. chat on Discord, however you like. Okay.
    chat on Discord, however you like. Okay.

    And uh oh yeah, one other thing that I And uh oh yeah, one other thing that I'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 34
  start_sec: 1562.48
  end_sec: 1603.679
  text: 'And uh oh yeah, one other thing that I

    need to mention there are a couple of need to mention there are a couple of need
    to mention there are a couple of

    people already done that but which you people already done that but which you
    people already done that but which you

    don''t need to. Uh you don''t need to don''t need to. Uh you don''t need to don''t
    need to. Uh you don''t need to

    submit official audit form. I know that submit official audit form. I know that
    submit official audit form. I know that

    your uh academic advisor probably asked your uh academic advisor probably asked
    your uh academic advisor probably asked

    you to do that. You don''t have to do you to do that. You don''t have to do you
    to do that. You don''t have to do

    that. I already confirmed. You don''t that. I already confirmed. You don''t that.
    I already confirmed. You don''t

    need to do that. Just just sit in class. need to do that. Just just sit in class.
    need to do that. Just just sit in class.

    It''s fine. Just don''t tell anyone. Well, It''s fine. Just don''t tell anyone.
    Well, It''s fine. Just don''t tell anyone. Well,

    no, you can tell everyone. It''s fine. no, you can tell everyone. It''s fine.
    no, you can tell everyone. It''s fine.

    Just it''s okay. Do not need to submit Just it''s okay. Do not need to submit
    Just it''s okay. Do not need to submit

    it. Um and uh yeah, so more details are it. Um and uh yeah, so more details are
    it. Um and uh yeah, so more details are

    you can find on the class website. Cool. you can find on the class website. Cool.
    you can find on the class website. Cool.

    All right. So, more things about All right. So, more things about All right. So,
    more things about

    logistics. Sorry, the logistics is logistics. Sorry, the logistics is logistics.
    Sorry, the logistics is

    really really long. Uh but basically really really long. Uh but basically really
    really long. Uh but basically

    this class will be entirely recorded and this class will be entirely recorded
    and this class will be entirely recorded and

    streamed on Zoom like we have seen here. streamed on Zoom like we have seen here.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 35
  start_sec: 1603.679
  end_sec: 1645.83
  text: 'streamed on Zoom like we have seen here.

    Thank you Jacob for doing that. Um so Thank you Jacob for doing that. Um so Thank
    you Jacob for doing that. Um so

    yeah so basically what you can do here yeah so basically what you can do here
    yeah so basically what you can do here

    is that you can if you don''t want to is that you can if you don''t want to is
    that you can if you don''t want to

    come to class although I would say come to class although I would say come to
    class although I would say

    coming to class should be fun. It''s like coming to class should be fun. It''s
    like coming to class should be fun. It''s like

    it''s 5:00 p.m. You should be able to, it''s 5:00 p.m. You should be able to,
    it''s 5:00 p.m. You should be able to,

    you know, get up by 5:00 p.m. Yeah. you know, get up by 5:00 p.m. Yeah. you know,
    get up by 5:00 p.m. Yeah.

    Anyway, uh but yeah, but if you don''t Anyway, uh but yeah, but if you don''t
    Anyway, uh but yeah, but if you don''t

    want to or like you''re traveling or want to or like you''re traveling or want
    to or like you''re traveling or

    something, yeah, feel free to watch it. something, yeah, feel free to watch it.
    something, yeah, feel free to watch it.

    uh from home and um I''ve already shared uh from home and um I''ve already shared
    uh from home and um I''ve already shared

    the link on the discord so you should be the link on the discord so you should
    be the link on the discord so you should be

    able to find it. Uh and afterwards if able to find it. Uh and afterwards if able
    to find it. Uh and afterwards if

    you want to rewatch the uh lecture or you want to rewatch the uh lecture or you
    want to rewatch the uh lecture or

    you didn''t come to class and then you you didn''t come to class and then you
    you didn''t come to class and then you

    want to watch it uh then you can access want to watch it uh then you can access
    want to watch it uh then you can access

    the recording through Ponapto'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 36
  start_sec: 1647.99
  end_sec: 1689.84
  text: 'Ponupto I don''t know uh like the the the Ponupto I don''t know uh like the
    the the

    thing that I also shared on Discord and thing that I also shared on Discord and
    thing that I also shared on Discord and

    later on we''re going to be posting the later on we''re going to be posting the
    later on we''re going to be posting the

    um like edited version of the recording um like edited version of the recording
    um like edited version of the recording

    on YouTube as well. So, if you have any on YouTube as well. So, if you have any
    on YouTube as well. So, if you have any

    concern about privacy and stuff, maybe concern about privacy and stuff, maybe
    concern about privacy and stuff, maybe

    try to sit in a place where you''re not try to sit in a place where you''re not
    try to sit in a place where you''re not

    going to be recorded. Although, I''m not going to be recorded. Although, I''m
    not going to be recorded. Although, I''m not

    sure if I feel like I feel like you''re sure if I feel like I feel like you''re
    sure if I feel like I feel like you''re

    going to be fine, honestly. Um, but going to be fine, honestly. Um, but going
    to be fine, honestly. Um, but

    yeah, just like let me know if you want yeah, just like let me know if you want
    yeah, just like let me know if you want

    to get edit out and stuff and then I to get edit out and stuff and then I to get
    edit out and stuff and then I

    I''ll do that. Cool. Uh, a few more I''ll do that. Cool. Uh, a few more I''ll
    do that. Cool. Uh, a few more

    things about resources is that I have things about resources is that I have things
    about resources is that I have

    listed a bunch of papers and it will be listed a bunch of papers and it will be
    listed a bunch of papers and it will be

    getting updated throughout the class as getting updated throughout the class as
    getting updated throughout the class as

    well on the class website. and uh just well on the class website. and uh just
    well on the class website. and uh just

    uh uh'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 37
  start_sec: 1689.84
  end_sec: 1730.559
  text: 'uh

    feel free to read it especially this one feel free to read it especially this
    one feel free to read it especially this one

    book uh so this book is written by a book uh so this book is written by a book
    uh so this book is written by a

    bunch of legends uh including like two bunch of legends uh including like two
    bunch of legends uh including like two

    of my co-authors uh when I was doing an of my co-authors uh when I was doing an
    of my co-authors uh when I was doing an

    internship at Sony and uh like two oh internship at Sony and uh like two oh internship
    at Sony and uh like two oh

    actually three of my co-authors at from actually three of my co-authors at from
    actually three of my co-authors at from

    Sony and two of my uh like mentors I Sony and two of my uh like mentors I Sony
    and two of my uh like mentors I

    guess uh from Stanford uh when I was at guess uh from Stanford uh when I was at
    guess uh from Stanford uh when I was at

    Stanford so they are all legendary Stanford so they are all legendary Stanford
    so they are all legendary

    people and that book is like super super people and that book is like super super
    people and that book is like super super

    well written uh so and we''re going to be well written uh so and we''re going
    to be well written uh so and we''re going to be

    kind of following the book although not kind of following the book although not
    kind of following the book although not

    ex ex ex

    exactly but like we''re going to be exactly but like we''re going to be exactly
    but like we''re going to be

    because Stephano taught me diffusion I because Stephano taught me diffusion I
    because Stephano taught me diffusion I

    guess so like the the the the the guess so like the the the the the guess so like
    the the the the the

    thought process the train of thought is thought process the train of thought is
    thought process the train of thought is

    going to be the same um yeah so feel going to be the same um yeah so feel'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 38
  start_sec: 1730.559
  end_sec: 1777.75
  text: 'going to be the same um yeah so feel

    free to read this book this is amazing free to read this book this is amazing
    free to read this book this is amazing

    uh and besides this class if you want to uh and besides this class if you want
    to uh and besides this class if you want to

    learn more about any of the learn more about any of the learn more about any of
    the

    that we are going to be covering uh that we are going to be covering uh that we
    are going to be covering uh

    there are a bunch of classes that''s like there are a bunch of classes that''s
    like there are a bunch of classes that''s like

    have their material available online have their material available online have
    their material available online

    from Stanford from Stanford from Stanford

    and also our CMU and also there''s one and also our CMU and also there''s one
    and also our CMU and also there''s one

    other class from MIT those are all great other class from MIT those are all great
    other class from MIT those are all great

    feel free to watch them um and there are feel free to watch them um and there
    are feel free to watch them um and there are

    also re written tutorials like blog also re written tutorials like blog also re
    written tutorials like blog

    posts that are basically just amazing uh posts that are basically just amazing
    uh posts that are basically just amazing uh

    and you should you should read them as and you should you should read them as
    and you should you should read them as

    well or you don''t have to but you know well or you don''t have to but you know
    well or you don''t have to but you know

    you should um and finally one last thing you should um and finally one last thing
    you should um and finally one last thing

    uh about the logistics is that the only uh about the logistics is that the only
    uh about the logistics is that the only

    goal in this class is for you to learn goal in this class is for you to learn
    goal in this class is for you to learn

    and diffusion and flow matching models.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 39
  start_sec: 1777.75
  end_sec: 1814.789
  text: 'and diffusion and flow matching models. and diffusion and flow matching models.

    Uh so nothing is important, nothing else Uh so nothing is important, nothing else
    Uh so nothing is important, nothing else

    is important. Uh which is why lecture is important. Uh which is why lecture is
    important. Uh which is why lecture

    attendance is not required. So you don''t attendance is not required. So you don''t
    attendance is not required. So you don''t

    need to come to class if you don''t want need to come to class if you don''t want
    need to come to class if you don''t want

    to. Um the only thing you need to do in to. Um the only thing you need to do in
    to. Um the only thing you need to do in

    person though is you need to take the person though is you need to take the person
    though is you need to take the

    quizzes in person. So like quizzes in person. So like quizzes in person. So like

    make sure that you come to class for the make sure that you come to class for
    the make sure that you come to class for the

    quizzes on the quiz days. Uh it''s just quizzes on the quiz days. Uh it''s just
    quizzes on the quiz days. Uh it''s just

    going to be the first 10 minutes of the going to be the first 10 minutes of the
    going to be the first 10 minutes of the

    class. Don''t be late though. It''s class. Don''t be late though. It''s class.
    Don''t be late though. It''s

    because it''s going to be the first 10 because it''s going to be the first 10
    because it''s going to be the first 10

    minute of the class and after taking the minute of the class and after taking
    the minute of the class and after taking the

    quiz, we''re going to collect papers and quiz, we''re going to collect papers
    and quiz, we''re going to collect papers and

    feel free to just go like from from feel free to just go like from from feel free
    to just go like from from

    there. You don''t you don''t need to sit there. You don''t you don''t need to
    sit there. You don''t you don''t need to sit

    in the class if you don''t want to. Uh I'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 40
  start_sec: 1814.789
  end_sec: 1851.909
  text: 'in the class if you don''t want to. Uh I in the class if you don''t want
    to. Uh I

    know I don''t like taking classes uh when know I don''t like taking classes uh
    when know I don''t like taking classes uh when

    I was a when I was a college student. So I was a when I was a college student.
    So I was a when I was a college student. So

    totally understandable. Um and uh your totally understandable. Um and uh your
    totally understandable. Um and uh your

    grade will only be curved up and never grade will only be curved up and never
    grade will only be curved up and never

    be curved down. So uh and also if be curved down. So uh and also if be curved
    down. So uh and also if

    everyone does well, everyone gets an A. everyone does well, everyone gets an A.
    everyone does well, everyone gets an A.

    Okay? So like there''s no competition in Okay? So like there''s no competition
    in Okay? So like there''s no competition in

    this class. everyone can get an A. Uh this class. everyone can get an A. Uh this
    class. everyone can get an A. Uh

    but we are going to be but because this but we are going to be but because this
    but we are going to be but because this

    is the first time that we''re teaching a is the first time that we''re teaching
    a is the first time that we''re teaching a

    class. Uh so we don''t really know what class. Uh so we don''t really know what
    class. Uh so we don''t really know what

    is a good like you know cuto off for A''s is a good like you know cuto off for
    A''s is a good like you know cuto off for A''s

    and stuff. So uh but we''re going to be and stuff. So uh but we''re going to be
    and stuff. So uh but we''re going to be

    announcing that probably midclassish so announcing that probably midclassish so
    announcing that probably midclassish so

    that you know you can you know maybe do that you know you can you know maybe do
    that you know you can you know maybe do

    some of my survey you know if you need'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 41
  start_sec: 1851.909
  end_sec: 1921.2
  text: 'some of my survey you know if you need some of my survey you know if you
    need

    some extra credits. Um but anyway um some extra credits. Um but anyway um some
    extra credits. Um but anyway um

    yeah but just in general feel free to yeah but just in general feel free to yeah
    but just in general feel free to

    use any and all resources that you can use any and all resources that you can
    use any and all resources that you can

    find. Okay, this is the end of the not find. Okay, this is the end of the not
    find. Okay, this is the end of the not

    the class. This is the end of the the class. This is the end of the the class.
    This is the end of the

    logistics. Anyone has any questions logistics. Anyone has any questions logistics.
    Anyone has any questions

    about logistics? Amazing. Amazing.

    Now, Cool. All right. Now, let''s uh get to Cool. All right. Now, let''s uh get
    to

    the real deal. Uh so first of all we''re the real deal. Uh so first of all we''re
    the real deal. Uh so first of all we''re

    going to be uh you know reviewing some going to be uh you know reviewing some
    going to be uh you know reviewing some

    of the basic knowledge that you probably of the basic knowledge that you probably
    of the basic knowledge that you probably

    already know uh but just in case we''re already know uh but just in case we''re
    already know uh but just in case we''re

    going to be covering that. So first of going to be covering that. So first of
    going to be covering that. So first of

    all we''re going to be doing uh all we''re going to be doing uh all we''re going
    to be doing uh

    probabilistic modeling in this class. Uh probabilistic modeling in this class.
    Uh probabilistic modeling in this class. Uh

    what is probabilistic modeling? Does what is probabilistic modeling? Does what
    is probabilistic modeling? Does

    anyone want to answer this question? Okay. So, you''re trying to model P of X
    Okay. So, you''re trying to model P of X

    given Y. Is that what you said? Okay. given Y. Is that what you said? Okay.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 42
  start_sec: 1921.2
  end_sec: 1984.23
  text: 'given Y. Is that what you said? Okay.

    So, but what is P? >> I mean, I guess I could model X. >> I mean, I guess I could
    model X.

    >> Okay. Yeah. Yeah. Yeah. Pretty much. >> Okay. Yeah. Yeah. Yeah. Pretty much.
    >> Okay. Yeah. Yeah. Yeah. Pretty much.

    Pretty much. But like uh so in general Pretty much. But like uh so in general
    Pretty much. But like uh so in general

    what is probability model is that I you what is probability model is that I you
    what is probability model is that I you

    I don''t know if everyone know this mean I don''t know if everyone know this mean
    I don''t know if everyone know this mean

    but like we do not do absolute we do it but like we do not do absolute we do it
    but like we do not do absolute we do it

    but maybe anyway uh so uh probability but maybe anyway uh so uh probability but
    maybe anyway uh so uh probability

    modeling is to model world with modeling is to model world with modeling is to
    model world with

    uncertainty because our world has a lot uncertainty because our world has a lot
    uncertainty because our world has a lot

    of uncertainties using probabilities. of uncertainties using probabilities. of
    uncertainties using probabilities.

    Haha. All right that''s it. Uh but but Haha. All right that''s it. Uh but but
    Haha. All right that''s it. Uh but but

    but uh so to give you an example it''s but uh so to give you an example it''s
    but uh so to give you an example it''s

    basically just a statements like this is basically just a statements like this
    is basically just a statements like this is

    like a probabilistic statement right? So like a probabilistic statement right?
    So like a probabilistic statement right? So

    like there is a 70% chance that it will like there is a 70% chance that it will
    like there is a 70% chance that it will

    rain tomorrow. All right. So we usually rain tomorrow. All right. So we usually
    rain tomorrow. All right. So we usually

    do probabilistic reasoning with P of X P do probabilistic reasoning with P of
    X P do probabilistic reasoning with P of X P

    of Y right what are they? So X and Y''s'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 43
  start_sec: 1984.23
  end_sec: 2027.12
  text: 'of Y right what are they? So X and Y''s of Y right what are they? So X and
    Y''s

    are random variables. So basically just are random variables. So basically just
    are random variables. So basically just

    the things that we''re trying to describe the things that we''re trying to describe
    the things that we''re trying to describe

    like tomorrow''s weather and they can be like tomorrow''s weather and they can
    be like tomorrow''s weather and they can be

    continuous like an image or they can be continuous like an image or they can be
    continuous like an image or they can be

    discrete like text and usually we denote discrete like text and usually we denote
    discrete like text and usually we denote

    them with like XYZ you know those like them with like XYZ you know those like
    them with like XYZ you know those like

    alphabet and uh the other thing that we alphabet and uh the other thing that we
    alphabet and uh the other thing that we

    need is a probab probability need is a probab probability need is a probab probability

    distribution basically just like how distribution basically just like how distribution
    basically just like how

    things are and how often they are as things are and how often they are as things
    are and how often they are as

    they are uh you know how often do these they are uh you know how often do these
    they are uh you know how often do these

    things happen. So, for example, uh a things happen. So, for example, uh a things
    happen. So, for example, uh a

    probability a probability distribution probability a probability distribution
    probability a probability distribution

    of the weather in Pittsburgh in the of the weather in Pittsburgh in the of the
    weather in Pittsburgh in the

    winter is going to be 50% chance snowy, winter is going to be 50% chance snowy,
    winter is going to be 50% chance snowy,

    50% chance cloudy. Today is one of those 50% chance cloudy. Today is one of those
    50% chance cloudy. Today is one of those

    cloudy days. Unfortunate. Well, I don''t cloudy days. Unfortunate. Well, I don''t
    cloudy days. Unfortunate. Well, I don''t

    know which one is more unfortunate know which one is more unfortunate'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 44
  start_sec: 2027.12
  end_sec: 2078.47
  text: 'know which one is more unfortunate

    actually. Um but uh basically we usually actually. Um but uh basically we usually
    actually. Um but uh basically we usually

    denote it as P of X. denote it as P of X. denote it as P of X.

    Do some combinations of the capital Do some combinations of the capital Do some
    combinations of the capital

    letters. Yeah. uh but usually okay so letters. Yeah. uh but usually okay so letters.
    Yeah. uh but usually okay so

    the way that I use it is basically uh the way that I use it is basically uh the
    way that I use it is basically uh

    capitaliz x means that the random capitaliz x means that the random capitaliz
    x means that the random

    variable and then small x means like one variable and then small x means like
    one variable and then small x means like one

    specific example this is usually how I specific example this is usually how I
    specific example this is usually how I

    do it right so there are a lot of uh some key right so there are a lot of uh some
    key

    concept in the probabilities theory that concept in the probabilities theory that
    concept in the probabilities theory that

    we can that we should be familiar with we can that we should be familiar with
    we can that we should be familiar with

    for this class. for this class. for this class.

    So the first thing is uh the joint So the first thing is uh the joint So the first
    thing is uh the joint

    distribution basically just like the distribution basically just like the distribution
    basically just like the

    distribution to describe um like how distribution to describe um like how distribution
    to describe um like how

    often and how X and Y both X and Y often and how X and Y both X and Y often and
    how X and Y both X and Y

    happen. Marginal distribution is when happen. Marginal distribution is when happen.
    Marginal distribution is when

    it''s sort of like in relation to the it''s sort of like in relation to the it''s
    sort of like in relation to the

    joint distribution when you only joint distribution when you only joint distribution
    when you only

    consider X or only consider Y. And the'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 45
  start_sec: 2078.47
  end_sec: 2121.75
  text: 'consider X or only consider Y. And the consider X or only consider Y. And
    the

    conditional distribution is when you are conditional distribution is when you
    are conditional distribution is when you are

    trying to determine like the trying to determine like the trying to determine
    like the

    distribution of X when you have an distribution of X when you have an distribution
    of X when you have an

    observation on Y or vice versa. And uh observation on Y or vice versa. And uh
    observation on Y or vice versa. And uh

    probably the most theory is this thing probably the most theory is this thing
    probably the most theory is this thing

    called beta theorem. Uh yeah, it''s so called beta theorem. Uh yeah, it''s so
    called beta theorem. Uh yeah, it''s so

    important that you should probably important that you should probably important
    that you should probably

    tattoo it or something. Uh but what''s tattoo it or something. Uh but what''s
    tattoo it or something. Uh but what''s

    happening is that basically it describes happening is that basically it describes
    happening is that basically it describes

    the relationship between the conditional the relationship between the conditional
    the relationship between the conditional

    distribution, joint distribution and the distribution, joint distribution and
    the distribution, joint distribution and the

    marginal. Uh so this is just saying that marginal. Uh so this is just saying that
    marginal. Uh so this is just saying that

    like the probability of X given Y is like the probability of X given Y is like
    the probability of X given Y is

    equal to you know how often do X and Y equal to you know how often do X and Y
    equal to you know how often do X and Y

    happen together divided by like the the happen together divided by like the the
    happen together divided by like the the

    original prob distribution of Y because original prob distribution of Y because
    original prob distribution of Y because

    you''re given Y already, right? So I feel you''re given Y already, right? So I
    feel you''re given Y already, right? So I feel

    like that kind of makes sense and if you like that kind of makes sense and if
    you like that kind of makes sense and if you

    just do a little bit of algebra you''re'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 46
  start_sec: 2121.75
  end_sec: 2171.76
  text: 'just do a little bit of algebra you''re just do a little bit of algebra you''re

    going to be able to get this very nice going to be able to get this very nice
    going to be able to get this very nice

    formula here. Okay cool. So in in beaian formula here. Okay cool. So in in beaian
    formula here. Okay cool. So in in beaian

    view we usually call like the basically view we usually call like the basically
    view we usually call like the basically

    the uh if the p of x as the prior the uh if the p of x as the prior the uh if
    the p of x as the prior

    basically it means that uh what I basically it means that uh what I basically
    it means that uh what I

    originally believe about the random originally believe about the random originally
    believe about the random

    variable x and the posterior is what I variable x and the posterior is what I
    variable x and the posterior is what I

    now believe about x now that I''ve seen now believe about x now that I''ve seen
    now believe about x now that I''ve seen

    some now that I''ve seen why. Uh so like some now that I''ve seen why. Uh so like
    some now that I''ve seen why. Uh so like

    the prior is like prior to your the prior is like prior to your the prior is like
    prior to your

    observation of y what you believe about observation of y what you believe about
    observation of y what you believe about

    x. Posterior is uh how I what I believe x. Posterior is uh how I what I believe
    x. Posterior is uh how I what I believe

    about x after I observe y. Okay. And the about x after I observe y. Okay. And
    the about x after I observe y. Okay. And the

    other thing uh is uh independence. This other thing uh is uh independence. This
    other thing uh is uh independence. This

    is basically just saying that uh knowing is basically just saying that uh knowing
    is basically just saying that uh knowing

    y tells you nothing about x or knowing x y tells you nothing about x or knowing
    x'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 47
  start_sec: 2171.76
  end_sec: 2221.829
  text: 'y tells you nothing about x or knowing x

    tells you nothing about y. So you uh tells you nothing about y. So you uh tells
    you nothing about y. So you uh

    just do not change your posterior. Oh just do not change your posterior. Oh just
    do not change your posterior. Oh

    sorry you do not change your prior at sorry you do not change your prior at sorry
    you do not change your prior at

    all. So basically your posterior is all. So basically your posterior is all. So
    basically your posterior is

    equal to your prior. It doesn''t like it equal to your prior. It doesn''t like
    it equal to your prior. It doesn''t like it

    doesn''t mean anything to you basically. doesn''t mean anything to you basically.
    doesn''t mean anything to you basically.

    Um yeah so that''s independence. Um yeah so that''s independence. Um yeah so that''s
    independence.

    Okay Okay Okay

    hopefully everyone are familiar with hopefully everyone are familiar with hopefully
    everyone are familiar with

    these concepts. Um but basically the these concepts. Um but basically the these
    concepts. Um but basically the

    goal of probability modeling is to learn goal of probability modeling is to learn
    goal of probability modeling is to learn

    those probability distribution about the those probability distribution about
    the those probability distribution about the

    random variables that we care about. Um random variables that we care about. Um
    random variables that we care about. Um

    so we can usually describe a probability so we can usually describe a probability
    so we can usually describe a probability

    distribution through some parameters and distribution through some parameters
    and distribution through some parameters and

    we usually denote them uh using some we usually denote them uh using some we usually
    denote them uh using some

    like just uh Greek alphabet instead of like just uh Greek alphabet instead of
    like just uh Greek alphabet instead of

    English alphabet. Um so for example uh English alphabet. Um so for example uh
    English alphabet. Um so for example uh

    for gausian we have parameter the mean for gausian we have parameter the mean
    for gausian we have parameter the mean

    and the variance as our parameter. For and the variance as our parameter. For
    and the variance as our parameter. For

    person distribution we have like the'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 48
  start_sec: 2221.829
  end_sec: 2277.27
  text: 'person distribution we have like the person distribution we have like the

    average rate as our uh parameter. average rate as our uh parameter. average rate
    as our uh parameter.

    Uh basically it''s just like the things Uh basically it''s just like the things
    Uh basically it''s just like the things

    that determines what the distribution that determines what the distribution that
    determines what the distribution

    look like and for some complicated look like and for some complicated look like
    and for some complicated

    distributions we can also parameterize distributions we can also parameterize
    distributions we can also parameterize

    it by some neuronet network which we it by some neuronet network which we it by
    some neuronet network which we

    usually denote as theta usually denote as theta usually denote as theta

    and the goal because like general goal and the goal because like general goal
    and the goal because like general goal

    of probabilistic modeling is to learn a of probabilistic modeling is to learn
    a of probabilistic modeling is to learn a

    probability distribution. If we are able probability distribution. If we are able
    probability distribution. If we are able

    to parameterize the distributions, then to parameterize the distributions, then
    to parameterize the distributions, then

    now the goal becomes to learn those now the goal becomes to learn those now the
    goal becomes to learn those

    parameters given some data that we parameters given some data that we parameters
    given some data that we

    observe. Uh and just a quick note that observe. Uh and just a quick note that
    observe. Uh and just a quick note that

    there''s also nonpar um nonparametric there''s also nonpar um nonparametric there''s
    also nonpar um nonparametric

    uh probability modeling but we''re just uh probability modeling but we''re just
    uh probability modeling but we''re just

    not going to be talking about it in this not going to be talking about it in this
    not going to be talking about it in this

    class. All right, cool. So class. All right, cool. So class. All right, cool.
    So

    uh like basically because we we want to uh like basically because we we want to
    uh like basically because we we want to

    learn the parameters given our data. So learn the parameters given our data. So
    learn the parameters given our data. So

    we call the probability of the data'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 49
  start_sec: 2277.27
  end_sec: 2368.8
  text: 'we call the probability of the data we call the probability of the data

    given our learn the model parameter as given our learn the model parameter as
    given our learn the model parameter as

    the likelihood basically just like under the likelihood basically just like under
    the likelihood basically just like under

    this model or like if my parameters of this model or like if my parameters of
    this model or like if my parameters of

    the models are accurate or if my model the models are accurate or if my model
    the models are accurate or if my model

    is accurate how likely is the data that is accurate how likely is the data that
    is accurate how likely is the data that

    I observed. So this is called I observed. So this is called I observed. So this
    is called

    likelihood. Okay. So now that we know what is Okay. So now that we know what is

    probabilistic modeling, what is probabilistic modeling, what is probabilistic
    modeling, what is

    generative modeling then? Anyone want to generative modeling then? Anyone want
    to generative modeling then? Anyone want to

    answer? You should know like you you you answer? You should know like you you
    you answer? You should know like you you you

    you use this every day. You use a gener you use this every day. You use a gener
    you use this every day. You use a gener

    model every day. model every day. model every day.

    Nobody knows. Ain''t no way. Okay. Yeah. >> Uh kind of. >> Uh kind of.

    Okay. Maybe >> kind of um kind of. So what? Okay, how >> kind of um kind of. So
    what? Okay, how

    about I change the question? What is the about I change the question? What is
    the about I change the question? What is the

    difference between difference between difference between

    generative modeling and discriminate generative modeling and discriminate generative
    modeling and discriminate

    discriminative modeling? >> Very close. Very close. Okay. So >> Very close. Very
    close. Okay. So

    basically what''s happening basically what''s happening basically what''s happening

    is that this is a famous quote from is that this is a famous quote from is that
    this is a famous quote from

    Richard Feman. Uh apparently people Richard Feman. Uh apparently people'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 50
  start_sec: 2368.8
  end_sec: 2406.64
  text: 'Richard Feman. Uh apparently people

    found it on his blackboard after he died found it on his blackboard after he died
    found it on his blackboard after he died

    or something. I don''t know if that after or something. I don''t know if that
    after or something. I don''t know if that after

    he did that or before he died but this he did that or before he died but this
    he did that or before he died but this

    is what they found on his blackboard. is what they found on his blackboard. is
    what they found on his blackboard.

    And what he said was um what I cannot And what he said was um what I cannot And
    what he said was um what I cannot

    create I do not understand. So create I do not understand. So create I do not
    understand. So

    generative modeling is basically the generative modeling is basically the generative
    modeling is basically the

    contraositive of this. It''s like contraositive of this. It''s like contraositive
    of this. It''s like

    what I understand I should be able to what I understand I should be able to what
    I understand I should be able to

    create. This is basically the idea of create. This is basically the idea of create.
    This is basically the idea of

    genetic modeling. Uh yeah, I copied this genetic modeling. Uh yeah, I copied this
    genetic modeling. Uh yeah, I copied this

    image from Stephanos''s class by the way. image from Stephanos''s class by the
    way. image from Stephanos''s class by the way.

    Okay, so basically let''s say we have Okay, so basically let''s say we have Okay,
    so basically let''s say we have

    some data that we did on SX and then we some data that we did on SX and then we
    some data that we did on SX and then we

    have some label that is associated with have some label that is associated with
    have some label that is associated with

    the data. So for example, say we have a the data. So for example, say we have
    a the data. So for example, say we have a

    bunch of images of a bedroom uh and then bunch of images of a bedroom uh and then'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 51
  start_sec: 2406.64
  end_sec: 2451.92
  text: 'bunch of images of a bedroom uh and then

    the label of the bedroom is whether or the label of the bedroom is whether or
    the label of the bedroom is whether or

    not it''s a luxurious bedroom. I''ve been not it''s a luxurious bedroom. I''ve
    been not it''s a luxurious bedroom. I''ve been

    looking at bedrooms in New York City is looking at bedrooms in New York City is
    looking at bedrooms in New York City is

    uh pretty amazing. Anyway, so uh uh pretty amazing. Anyway, so uh uh pretty amazing.
    Anyway, so uh

    discriminative modeling is basically the discriminative modeling is basically
    the discriminative modeling is basically the

    goal is to learn uh basically to to goal is to learn uh basically to to goal is
    to learn uh basically to to

    determine the the the label based on the determine the the the label based on
    the determine the the the label based on the

    image uh based on the data. So basically image uh based on the data. So basically
    image uh based on the data. So basically

    it''s like we want to be able to it''s like we want to be able to it''s like we
    want to be able to

    determine if a bedroom is luxurious determine if a bedroom is luxurious determine
    if a bedroom is luxurious

    given the image. So in this case the given the image. So in this case the given
    the image. So in this case the

    image or the image or the image or the

    data is given in discriminative modeling data is given in discriminative modeling
    data is given in discriminative modeling

    and the generary modeling the goal is to and the generary modeling the goal is
    to and the generary modeling the goal is to

    learn either the joint distribution learn either the joint distribution learn
    either the joint distribution

    between the uh image between data and between the uh image between data and between
    the uh image between data and

    the label or just the distribution of the label or just the distribution of the
    label or just the distribution of

    the data itself. Uh so basically what the data itself. Uh so basically what the
    data itself. Uh so basically what

    we''re trying to learn is what a bedroom we''re trying to learn is what a bedroom'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 52
  start_sec: 2451.92
  end_sec: 2496.079
  text: 'we''re trying to learn is what a bedroom

    should look like or what a luxurious or should look like or what a luxurious or
    should look like or what a luxurious or

    what a cheap I guess uh bedroom should what a cheap I guess uh bedroom should
    what a cheap I guess uh bedroom should

    look like and in this case the image is look like and in this case the image is
    look like and in this case the image is

    not given. So the model will need to be not given. So the model will need to be
    not given. So the model will need to be

    able to imagine uh what bedroom look able to imagine uh what bedroom look able
    to imagine uh what bedroom look

    like. So that''s why it''s like like. So that''s why it''s like like. So that''s
    why it''s like

    generative. Um yeah. So in general or generative. Um yeah. So in general or generative.
    Um yeah. So in general or

    more formally I guess not that formal uh more formally I guess not that formal
    uh more formally I guess not that formal uh

    is that given a set of data and some is that given a set of data and some is that
    given a set of data and some

    prior knowledge and assumption about prior knowledge and assumption about prior
    knowledge and assumption about

    your data. Uh what do you mean by pri oh your data. Uh what do you mean by pri
    oh your data. Uh what do you mean by pri oh

    I guess data are just like samples or I guess data are just like samples or I
    guess data are just like samples or

    like images basically. uh and what what like images basically. uh and what what
    like images basically. uh and what what

    do what do we mean by prior knowledge do what do we mean by prior knowledge do
    what do we mean by prior knowledge

    and assumptions? Basically just like and assumptions? Basically just like and
    assumptions? Basically just like

    what do we believe this uh distribution what do we believe this uh distribution
    what do we believe this uh distribution

    should be? So basically do we believe should be? So basically do we believe'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 53
  start_sec: 2496.079
  end_sec: 2546.87
  text: 'should be? So basically do we believe

    this is a gausian? Do we believe this is this is a gausian? Do we believe this
    is this is a gausian? Do we believe this is

    a mixture of gausian? Uh what kind of a mixture of gausian? Uh what kind of a
    mixture of gausian? Uh what kind of

    like parameterization that we should like parameterization that we should like
    parameterization that we should

    take and what kind of loss functions take and what kind of loss functions take
    and what kind of loss functions

    that we should use? What kind of like that we should use? What kind of like that
    we should use? What kind of like

    optimizations that we should use to optimizations that we should use to optimizations
    that we should use to

    learn this model? learn this model? learn this model?

    And um basically given all those things And um basically given all those things
    And um basically given all those things

    we want to learn a probability we want to learn a probability we want to learn
    a probability

    distribution that''s parameterized by distribution that''s parameterized by distribution
    that''s parameterized by

    some model that''s some model that''s some model that''s

    parameter theta such that uh this model parameter theta such that uh this model
    parameter theta such that uh this model

    should be able to do generation like should be able to do generation like should
    be able to do generation like

    basically if we we should be able to basically if we we should be able to basically
    if we we should be able to

    sample a new data point from this sample a new data point from this sample a new
    data point from this

    distribution and this sample should look distribution and this sample should look
    distribution and this sample should look

    like a real thing. So basically it like a real thing. So basically it like a real
    thing. So basically it

    should look like a real image of of the should look like a real image of of the
    should look like a real image of of the

    bedroom. Uh and you bedroom. Uh and you bedroom. Uh and you

    will probably want to although not will probably want to although not will probably
    want to although not

    necessarily able to uh be able to tell'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 54
  start_sec: 2546.87
  end_sec: 2586.319
  text: 'necessarily able to uh be able to tell necessarily able to uh be able to
    tell

    like how likely are your uh like is some like how likely are your uh like is some
    like how likely are your uh like is some

    data. So for example given an existing data. So for example given an existing
    data. So for example given an existing

    data point like say given an existing data point like say given an existing data
    point like say given an existing

    image you should be able to tell whether image you should be able to tell whether
    image you should be able to tell whether

    or not it look like a bedroom. So you or not it look like a bedroom. So you or
    not it look like a bedroom. So you

    should be able to assign a probability should be able to assign a probability
    should be able to assign a probability

    to it and the probability should be high to it and the probability should be high
    to it and the probability should be high

    when X looks real or look like if when X looks real or look like if when X looks
    real or look like if

    distribution. Uh and then the last thing distribution. Uh and then the last thing
    distribution. Uh and then the last thing

    which is like which is like which is like

    kind of not very trendy right now but uh kind of not very trendy right now but
    uh kind of not very trendy right now but uh

    we this is also sort of like a we this is also sort of like a we this is also
    sort of like a

    unsupervised learning way like we just unsupervised learning way like we just
    unsupervised learning way like we just

    learn everything by looking at the data learn everything by looking at the data
    learn everything by looking at the data

    and we don''t like if we just want to and we don''t like if we just want to and
    we don''t like if we just want to

    learn P of X we don''t really need any learn P of X we don''t really need any
    learn P of X we don''t really need any

    labeling or like uh annotations and labeling or like uh annotations and'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 55
  start_sec: 2586.319
  end_sec: 2645.43
  text: 'labeling or like uh annotations and

    stuff like that. Okay, stuff like that. Okay, stuff like that. Okay,

    cool. So how to train your generated cool. So how to train your generated cool.
    So how to train your generated

    models? Uh does anyone want to take a models? Uh does anyone want to take a models?
    Uh does anyone want to take a

    guess? All right. Basically uh if you think All right. Basically uh if you think

    about it right uh this this this about it right uh this this this about it right
    uh this this this

    particular sentence that we uh underline particular sentence that we uh underline
    particular sentence that we uh underline

    is the key right. So like the idea is is the key right. So like the idea is is
    the key right. So like the idea is

    that uh you should assign high that uh you should assign high that uh you should
    assign high

    probability if the data looks real and probability if the data looks real and
    probability if the data looks real and

    you have a bunch of real data already. you have a bunch of real data already.
    you have a bunch of real data already.

    So the first idea is to maximize the So the first idea is to maximize the So the
    first idea is to maximize the

    like hhood like hhood like hhood

    of your existing data which is called of your existing data which is called of
    your existing data which is called

    like um maximum likelihood training I like um maximum likelihood training I like
    um maximum likelihood training I

    guess. Uh so basically what is happening guess. Uh so basically what is happening
    guess. Uh so basically what is happening

    is that remember how we call the is that remember how we call the is that remember
    how we call the

    probability of data given the model probability of data given the model probability
    of data given the model

    parameter as the likelihood. Uh and uh parameter as the likelihood. Uh and uh
    parameter as the likelihood. Uh and uh

    yeah so if my yeah so if my yeah so if my

    so that basically just means that like so that basically just means that like
    so that basically just means that like

    if my um parameters are correct then the'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 56
  start_sec: 2645.43
  end_sec: 2692.48
  text: 'if my um parameters are correct then the if my um parameters are correct
    then the

    real data point should have high real data point should have high real data point
    should have high

    likelihood. Uh which just means that we likelihood. Uh which just means that we
    likelihood. Uh which just means that we

    should just maximize likelihood of should just maximize likelihood of should just
    maximize likelihood of

    existing data because they''re all real. existing data because they''re all real.
    existing data because they''re all real.

    Uh so mathematically kind of given a Uh so mathematically kind of given a Uh so
    mathematically kind of given a

    data set we want to find the best uh data set we want to find the best uh data
    set we want to find the best uh

    parameter that can like that can parameter that can like that can parameter that
    can like that can

    maximize the likelihood of all the maximize the likelihood of all the maximize
    the likelihood of all the

    existing data that we have under the existing data that we have under the existing
    data that we have under the

    model. That''s pretty much it. Okay. model. That''s pretty much it. Okay. model.
    That''s pretty much it. Okay.

    Uh so if you think about it right let''s Uh so if you think about it right let''s
    Uh so if you think about it right let''s

    just consider a single data point from just consider a single data point from
    just consider a single data point from

    for for now and let''s say we know that for for now and let''s say we know that
    for for now and let''s say we know that

    data point is composed by a bunch of data point is composed by a bunch of data
    point is composed by a bunch of

    like smaller elements so for example uh like smaller elements so for example uh
    like smaller elements so for example uh

    like a sentence or a piece of text is like a sentence or a piece of text is like
    a sentence or a piece of text is

    composed by a bunch of tokens right or composed by a bunch of tokens right or
    composed by a bunch of tokens right or

    image is composed by a bunch of um image is composed by a bunch of um'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 57
  start_sec: 2692.48
  end_sec: 2739.92
  text: 'image is composed by a bunch of um

    pixels pixels pixels

    uh then um by the probability chain rule uh then um by the probability chain rule
    uh then um by the probability chain rule

    which just means that we break it up which just means that we break it up which
    just means that we break it up

    piece by piece piece by piece piece by piece

    uh then we should be able to get this. uh then we should be able to get this.
    uh then we should be able to get this.

    So this is the probability chain rule So this is the probability chain rule So
    this is the probability chain rule

    which means that like if you know that which means that like if you know that
    which means that like if you know that

    your like data is composed by like a your like data is composed by like a your
    like data is composed by like a

    bunch of small elements you should be bunch of small elements you should be bunch
    of small elements you should be

    able to um you should be able to use able to um you should be able to use able
    to um you should be able to use

    like the bay rule that the first part of like the bay rule that the first part
    of like the bay rule that the first part of

    bay rule I guess uh to bay rule I guess uh to bay rule I guess uh to

    uh to to get like a decomposed version uh to to get like a decomposed version
    uh to to get like a decomposed version

    of your likelihood of your likelihood of your likelihood

    and then uh basically you should be able and then uh basically you should be able
    and then uh basically you should be able

    to get uh because you you take the log to get uh because you you take the log
    to get uh because you you take the log

    and all the the the multiplication and all the the the multiplication and all
    the the the multiplication

    becomes uh summation and you should be becomes uh summation and you should be
    becomes uh summation and you should be

    able to get this thing that is very nice able to get this thing that is very nice'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 58
  start_sec: 2739.92
  end_sec: 2783.75
  text: 'able to get this thing that is very nice

    where the log likely the conditional log where the log likely the conditional
    log where the log likely the conditional log

    likelihood of your case element is only likelihood of your case element is only
    likelihood of your case element is only

    depending on everything that you have depending on everything that you have depending
    on everything that you have

    seen before. Uh so basically if you take seen before. Uh so basically if you take
    seen before. Uh so basically if you take

    on the entire data set you just like on the entire data set you just like on the
    entire data set you just like

    literally add another you just literally literally add another you just literally
    literally add another you just literally

    add another you you add up all the log add another you you add up all the log
    add another you you add up all the log

    likelihood of all the data that you have likelihood of all the data that you have
    likelihood of all the data that you have

    in in your data set and uh this is just in in your data set and uh this is just
    in in your data set and uh this is just

    like algebra. You basically just be like like algebra. You basically just be like
    like algebra. You basically just be like

    I time one here and then I can time zero I time one here and then I can time zero
    I time one here and then I can time zero

    and add something to it. But this thing and add something to it. But this thing
    and add something to it. But this thing

    happened to be the cross entropy loss happened to be the cross entropy loss happened
    to be the cross entropy loss

    when your ground truth label are one when your ground truth label are one when
    your ground truth label are one

    hot. And for those of you who do LM hot. And for those of you who do LM hot. And
    for those of you who do LM

    research, this is exactly how we train research, this is exactly how we train
    research, this is exactly how we train

    LLMs. Yes, we got LM already. Yeah,'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 59
  start_sec: 2783.75
  end_sec: 2827.28
  text: 'LLMs. Yes, we got LM already. Yeah, LLMs. Yes, we got LM already. Yeah,

    super easy. This is why people love it. super easy. This is why people love it.
    super easy. This is why people love it.

    Um, yeah. So like LM is literally just Um, yeah. So like LM is literally just
    Um, yeah. So like LM is literally just

    auto this is what we call auto auto this is what we call auto auto this is what
    we call auto

    reggressive modeling where you break reggressive modeling where you break reggressive
    modeling where you break

    things up piece by piece and then each things up piece by piece and then each
    things up piece by piece and then each

    components only depending the log components only depending the log components
    only depending the log

    likelihood of each components depending likelihood of each components depending
    likelihood of each components depending

    on everything you have calculated before on everything you have calculated before
    on everything you have calculated before

    and you just kind of add them up and and you just kind of add them up and and
    you just kind of add them up and

    then that''s valid basically and that''s then that''s valid basically and that''s
    then that''s valid basically and that''s

    that works. that that builds your that works. that that builds your that works.
    that that builds your

    homework. Uh basically. All right. Um so homework. Uh basically. All right. Um
    so homework. Uh basically. All right. Um so

    and then another thing that we can do to and then another thing that we can do
    to and then another thing that we can do to

    do general modeling is that uh notice do general modeling is that uh notice do
    general modeling is that uh notice

    how like a lot of things in the world how like a lot of things in the world how
    like a lot of things in the world

    are sort of like determined by some what are sort of like determined by some what
    are sort of like determined by some what

    we call latent variables is things that we call latent variables is things that
    we call latent variables is things that

    we cannot see directly. Uh so for we cannot see directly. Uh so for'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 60
  start_sec: 2827.28
  end_sec: 2872.72
  text: 'we cannot see directly. Uh so for

    example how a person look is largely example how a person look is largely example
    how a person look is largely

    determined by their genes which is not determined by their genes which is not
    determined by their genes which is not

    observable directly. Um there are a lot observable directly. Um there are a lot
    observable directly. Um there are a lot

    of variability of like how people can of variability of like how people can of
    variability of like how people can

    look but the genes are sort of just look but the genes are sort of just look but
    the genes are sort of just

    combinatorial right uh but the problem combinatorial right uh but the problem
    combinatorial right uh but the problem

    is we cannot observe the genes so we is we cannot observe the genes so we is we
    cannot observe the genes so we

    can''t just like uh give me your genes can''t just like uh give me your genes
    can''t just like uh give me your genes

    then it''s not not possible right so uh then it''s not not possible right so uh
    then it''s not not possible right so uh

    but like can we still take into account but like can we still take into account
    but like can we still take into account

    of the fact that there is like a hidden of the fact that there is like a hidden
    of the fact that there is like a hidden

    variable that will influence how a variable that will influence how a variable
    that will influence how a

    person look when we try to model say person look when we try to model say person
    look when we try to model say

    human face images which is what you''re human face images which is what you''re
    human face images which is what you''re

    going to do in homework by the way um So going to do in homework by the way um
    So going to do in homework by the way um So

    uh introducing VAE this is like such a uh introducing VAE this is like such a
    uh introducing VAE this is like such a

    such a beautiful paper. I was like oh my such a beautiful paper. I was like oh
    my'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 61
  start_sec: 2872.72
  end_sec: 2917.91
  text: 'such a beautiful paper. I was like oh my

    god this this thing is like who who god this this thing is like who who god this
    this thing is like who who

    thought of this thing? This is like thought of this thing? This is like thought
    of this thing? This is like

    genius like back back in the day back in genius like back back in the day back
    in genius like back back in the day back in

    the day like more than a decade ago. the day like more than a decade ago. the
    day like more than a decade ago.

    Anyway, so basically what we do uh to Anyway, so basically what we do uh to Anyway,
    so basically what we do uh to

    model this sort of like latent variable model this sort of like latent variable
    model this sort of like latent variable

    is that like given some data X, what we is that like given some data X, what we
    is that like given some data X, what we

    do is we sort of try to learn an encoder do is we sort of try to learn an encoder
    do is we sort of try to learn an encoder

    to encode say a human face image into to encode say a human face image into to
    encode say a human face image into

    the latent space which is like your the latent space which is like your the latent
    space which is like your

    genes or something but just some latent genes or something but just some latent
    genes or something but just some latent

    variable that we cannot see. Uh and then variable that we cannot see. Uh and then
    variable that we cannot see. Uh and then

    uh like we try and then we''ll try to uh like we try and then we''ll try to uh
    like we try and then we''ll try to

    decode it and back into a reconstruction decode it and back into a reconstruction
    decode it and back into a reconstruction

    version of the data. Uh so doing that version of the data. Uh so doing that version
    of the data. Uh so doing that

    right then now instead of only right then now instead of only right then now instead
    of only

    maximizing the likelihood of the data we'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 62
  start_sec: 2917.91
  end_sec: 2959.349
  text: 'maximizing the likelihood of the data we maximizing the likelihood of the
    data we

    also need to do another thing which is also need to do another thing which is
    also need to do another thing which is

    to make sure that the Z that the latent to make sure that the Z that the latent
    to make sure that the Z that the latent

    variable that we get from encoding the X variable that we get from encoding the
    X variable that we get from encoding the X

    is actually going to be able to decode. is actually going to be able to decode.
    is actually going to be able to decode.

    We''re actually going to be able to We''re actually going to be able to We''re
    actually going to be able to

    decode it into the same X. Right? So decode it into the same X. Right? So decode
    it into the same X. Right? So

    basically you just need to make sure basically you just need to make sure basically
    you just need to make sure

    that the Z that you encode it here and that the Z that you encode it here and
    that the Z that you encode it here and

    you actually need to be able to decode you actually need to be able to decode
    you actually need to be able to decode

    it into it into it into

    uh like a like like the same image. The uh like a like like the same image. The
    uh like a like like the same image. The

    problem though is that you do not know problem though is that you do not know
    problem though is that you do not know

    what Z is, right? It''s not it''s hidden. what Z is, right? It''s not it''s hidden.
    what Z is, right? It''s not it''s hidden.

    You do not have any supervision on that. You do not have any supervision on that.
    You do not have any supervision on that.

    So how do we learn this? Right? Uh so So how do we learn this? Right? Uh so So
    how do we learn this? Right? Uh so

    basically uh the idea here is to match basically uh the idea here is to match
    basically uh the idea here is to match

    two distributions. So we''re trying to'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 63
  start_sec: 2959.349
  end_sec: 3004.559
  text: 'two distributions. So we''re trying to two distributions. So we''re trying
    to

    minimize the difference between the minimize the difference between the minimize
    the difference between the

    distribution of Z given X that is distribution of Z given X that is distribution
    of Z given X that is

    induced by the encoder and then also the induced by the encoder and then also
    the induced by the encoder and then also the

    distribution of Z given X but induced by distribution of Z given X but induced
    by distribution of Z given X but induced by

    the decoder. Uh so how do we do that the decoder. Uh so how do we do that the
    decoder. Uh so how do we do that

    right? Uh the first thing that we need right? Uh the first thing that we need
    right? Uh the first thing that we need

    to know is like how to measure sort of to know is like how to measure sort of
    to know is like how to measure sort of

    like the difference between the like the difference between the like the difference
    between the

    distributions. Uh we cannot really distributions. Uh we cannot really distributions.
    Uh we cannot really

    directly use geometric difference directly use geometric difference directly use
    geometric difference

    between two points right because that between two points right because that between
    two points right because that

    doesn''t really make any sense. Uh so doesn''t really make any sense. Uh so doesn''t
    really make any sense. Uh so

    instead we use something called instead we use something called instead we use
    something called

    probability divergence and what it means probability divergence and what it means
    probability divergence and what it means

    is basically just like it''s it''s like is basically just like it''s it''s like
    is basically just like it''s it''s like

    it''s a function where you take two it''s a function where you take two it''s
    a function where you take two

    probability distributions as input and probability distributions as input and
    probability distributions as input and

    uh you need to be able to properly uh you need to be able to properly uh you need
    to be able to properly

    measure it by like so all the divergence measure it by like so all the divergence'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 64
  start_sec: 3004.559
  end_sec: 3053.2
  text: 'measure it by like so all the divergence

    that you output should be greater than that you output should be greater than
    that you output should be greater than

    zero and it should only be equal greater zero and it should only be equal greater
    zero and it should only be equal greater

    than or equal to zero and it should only than or equal to zero and it should only
    than or equal to zero and it should only

    be equal to zero if and only if the two be equal to zero if and only if the two
    be equal to zero if and only if the two

    distribution are the same distribution. distribution are the same distribution.
    distribution are the same distribution.

    And notice that unlike you know And notice that unlike you know And notice that
    unlike you know

    traditional distance it doesn''t need to traditional distance it doesn''t need
    to traditional distance it doesn''t need to

    be symmetric although there are some be symmetric although there are some be symmetric
    although there are some

    probability divergence that are probability divergence that are probability divergence
    that are

    symmetric. Uh but anyway uh one of the symmetric. Uh but anyway uh one of the
    symmetric. Uh but anyway uh one of the

    most popular ones is called the KL most popular ones is called the KL most popular
    ones is called the KL

    divergence divergence divergence

    uh which is basically just this uh which is basically just this uh which is basically
    just this

    particular uh formula and intuitively particular uh formula and intuitively particular
    uh formula and intuitively

    what it means is that if the world what it means is that if the world what it
    means is that if the world

    actually works like P like if the world actually works like P like if the world
    actually works like P like if the world

    is actually distributed by P how is actually distributed by P how is actually
    distributed by P how

    surprised we''re going to be if we model surprised we''re going to be if we model
    surprised we''re going to be if we model

    it like Q. Uh that''s that''s basically it like Q. Uh that''s that''s basically
    it like Q. Uh that''s that''s basically

    kind of the intuition. Uh but basically kind of the intuition. Uh but basically'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 65
  start_sec: 3053.2
  end_sec: 3101.75
  text: 'kind of the intuition. Uh but basically

    what''s going to happen here is that what''s going to happen here is that what''s
    going to happen here is that

    we''re going to be using the KL we''re going to be using the KL we''re going to
    be using the KL

    divergence to model the difference I divergence to model the difference I divergence
    to model the difference I

    guess between the uh probability of Z guess between the uh probability of Z guess
    between the uh probability of Z

    given X induced by the encoder and the given X induced by the encoder and the
    given X induced by the encoder and the

    probability of Z gum X induced by the probability of Z gum X induced by the probability
    of Z gum X induced by the

    decoder. Uh so basically literally decoder. Uh so basically literally decoder.
    Uh so basically literally

    writing it out uh in math is like so you writing it out uh in math is like so
    you writing it out uh in math is like so you

    still have your uh maximum likelihood still have your uh maximum likelihood still
    have your uh maximum likelihood

    objective but now you also need to try objective but now you also need to try
    objective but now you also need to try

    to like enforce this like correspondence to like enforce this like correspondence
    to like enforce this like correspondence

    essentially between the encoder and essentially between the encoder and essentially
    between the encoder and

    decoder and if you do some algebra decoder and if you do some algebra decoder
    and if you do some algebra

    you''re actually going to get this thing. you''re actually going to get this thing.
    you''re actually going to get this thing.

    So this thing has two parts. The first So this thing has two parts. The first
    So this thing has two parts. The first

    part is what we call the encoder decoder part is what we call the encoder decoder
    part is what we call the encoder decoder

    reconstruction loss which is basically reconstruction loss which is basically
    reconstruction loss which is basically

    like how accurate your X is going to be like how accurate your X is going to be
    like how accurate your X is going to be

    when you''re trying to decode it given'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 66
  start_sec: 3101.75
  end_sec: 3149.359
  text: 'when you''re trying to decode it given when you''re trying to decode it given

    unz and then the other thing is what we unz and then the other thing is what we
    unz and then the other thing is what we

    call the kale regularization basically call the kale regularization basically
    call the kale regularization basically

    just like do not go too far from your uh just like do not go too far from your
    uh just like do not go too far from your uh

    from your prior basically uh and the two from your prior basically uh and the
    two from your prior basically uh and the two

    things combined together is what we call things combined together is what we call
    things combined together is what we call

    an elbow so evidence lower bound an elbow so evidence lower bound an elbow so
    evidence lower bound

    there are two ways to derive the elbow there are two ways to derive the elbow
    there are two ways to derive the elbow

    both I''m going to talk about both of both I''m going to talk about both of both
    I''m going to talk about both of

    them basically uh the first way is this them basically uh the first way is this
    them basically uh the first way is this

    so like you have your log likelihood so like you have your log likelihood so like
    you have your log likelihood

    here and then be and then basically you here and then be and then basically you
    here and then be and then basically you

    can just do log likelihood times one can just do log likelihood times one can
    just do log likelihood times one

    which is equal to the summation of your which is equal to the summation of your
    which is equal to the summation of your

    uh Q probability and this is why you can uh Q probability and this is why you
    can uh Q probability and this is why you can

    write it into like a sort of like a like write it into like a sort of like a like
    write it into like a sort of like a like

    a expectation of this thing and then a expectation of this thing and then'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 67
  start_sec: 3149.359
  end_sec: 3196.64
  text: 'a expectation of this thing and then

    like By bas rule again you are going to like By bas rule again you are going to
    like By bas rule again you are going to

    be able to get from the log px is be able to get from the log px is be able to
    get from the log px is

    equivalent to the log of p x n z divided equivalent to the log of p x n z divided
    equivalent to the log of p x n z divided

    by the the p of z given x. So this is by the the p of z given x. So this is by
    the the p of z given x. So this is

    literally just basultly literally just basultly literally just basultly

    this by this is equal to the joint right this by this is equal to the joint right
    this by this is equal to the joint right

    and then what you do is you uh multiply and then what you do is you uh multiply
    and then what you do is you uh multiply

    and divide it by this is like the and divide it by this is like the and divide
    it by this is like the

    greatest mathematical trick you multiply greatest mathematical trick you multiply
    greatest mathematical trick you multiply

    by something and divide it by the same by something and divide it by the same
    by something and divide it by the same

    thing or you plus something and divide thing or you plus something and divide
    thing or you plus something and divide

    it and minus the same thing. So it and minus the same thing. So it and minus the
    same thing. So

    basically you multiply Q of Z given S basically you multiply Q of Z given S basically
    you multiply Q of Z given S

    and divided by Q Z given S. But somehow and divided by Q Z given S. But somehow
    and divided by Q Z given S. But somehow

    magically this this thing breaks your um magically this this thing breaks your
    um magically this this thing breaks your um

    likelihood into two parts. So the first likelihood into two parts. So the first
    likelihood into two parts. So the first

    part is the the elbow part is the the elbow'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 68
  start_sec: 3196.64
  end_sec: 3247.91
  text: 'part is the the elbow

    the elbow. The second part is the kale the elbow. The second part is the kale
    the elbow. The second part is the kale

    divergence that we''re trying to uh divergence that we''re trying to uh divergence
    that we''re trying to uh

    minimize. minimize. minimize.

    So why is this the elbow? Well, this is So why is this the elbow? Well, this is
    So why is this the elbow? Well, this is

    basically because you can do some basically because you can do some basically
    because you can do some

    algebra here. So log of something algebra here. So log of something algebra here.
    So log of something

    divided by something is equivalent to divided by something is equivalent to divided
    by something is equivalent to

    log of something minus the log of that log of something minus the log of that
    log of something minus the log of that

    thing. Uh and then you just like break thing. Uh and then you just like break
    thing. Uh and then you just like break

    everything up with bay rule. This is why everything up with bay rule. This is
    why everything up with bay rule. This is why

    I say you should probably tattoo be rule I say you should probably tattoo be rule
    I say you should probably tattoo be rule

    somewhere, you know, just like look at somewhere, you know, just like look at
    somewhere, you know, just like look at

    it on your wrist or something like it''s it on your wrist or something like it''s
    it on your wrist or something like it''s

    you''re just going to use it so much. Uh you''re just going to use it so much.
    Uh you''re just going to use it so much. Uh

    and then and yeah, so bas uh basically. All right. The second way uh basically.
    All right. The second way

    to derive the same elbow is by uh to derive the same elbow is by uh to derive
    the same elbow is by uh

    basically observing that the p of x is basically observing that the p of x is
    basically observing that the p of x is

    equivalent to if this is a continuous equivalent to if this is a continuous equivalent
    to if this is a continuous

    distribution uh like then it''s just'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 69
  start_sec: 3247.91
  end_sec: 3303.76
  text: 'distribution uh like then it''s just distribution uh like then it''s just

    going to be like the the the the going to be like the the the the going to be
    like the the the the

    integral of the the joint uh dz and then integral of the the joint uh dz and then
    integral of the the joint uh dz and then

    again the greatest mathematical trick in again the greatest mathematical trick
    in again the greatest mathematical trick in

    the world multiply by something divided the world multiply by something divided
    the world multiply by something divided

    by something uh and then because you''re by something uh and then because you''re
    by something uh and then because you''re

    multiplying basically the integral of q multiplying basically the integral of
    q multiplying basically the integral of q

    something d qz something dz is the is something d qz something dz is the is something
    d qz something dz is the is

    the expectation. So you get a log of the expectation. So you get a log of the
    expectation. So you get a log of

    expectation of some ratio here and then expectation of some ratio here and then
    expectation of some ratio here and then

    this thing why do we have a like a this thing why do we have a like a this thing
    why do we have a like a

    inequality here? Anyone can does anyone inequality here? Anyone can does anyone
    inequality here? Anyone can does anyone

    take a guess why do we have an take a guess why do we have an take a guess why
    do we have an

    inequality here? inequality here? inequality here?

    Yeah Yeah Yeah

    I sorry I saw someone raised their hand. I sorry I saw someone raised their hand.
    I sorry I saw someone raised their hand.

    Yeah Yeah

    exactly is because of Jensen''s exactly is because of Jensen''s exactly is because
    of Jensen''s

    inequality. And why is it greater than inequality. And why is it greater than
    inequality. And why is it greater than

    or equal to? or equal to? or equal to?

    >> Because we function function is >> Because we function function is >> Because
    we function function is

    >> yeah because the because log is concave. >> yeah because the because log is
    concave.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 70
  start_sec: 3303.76
  end_sec: 3351.67
  text: '>> yeah because the because log is concave.

    Yeah, that''s right. Uh so yeah, Jensen Yeah, that''s right. Uh so yeah, Jensen
    Yeah, that''s right. Uh so yeah, Jensen

    inequality here and we get an inequality here and we get an inequality here and
    we get an

    inequality. Uh and uh if you expand this inequality. Uh and uh if you expand this
    inequality. Uh and uh if you expand this

    out out out

    becomes the elbow again. Yeah. So that''s becomes the elbow again. Yeah. So that''s
    becomes the elbow again. Yeah. So that''s

    this is how you derive elbow in two this is how you derive elbow in two this is
    how you derive elbow in two

    ways. Um but yeah basically the the core ways. Um but yeah basically the the core
    ways. Um but yeah basically the the core

    things that you need to the core things that you need to the core things that
    you need to the core

    mathematical trick that you need to mathematical trick that you need to mathematical
    trick that you need to

    remember from this derivation is that a remember from this derivation is that
    a remember from this derivation is that a

    bay rule is very important b you should bay rule is very important b you should
    bay rule is very important b you should

    try to think about how like if you''re try to think about how like if you''re
    try to think about how like if you''re

    get if you get stuck divide by something get if you get stuck divide by something
    get if you get stuck divide by something

    and multiply by the same thing or plus and multiply by the same thing or plus
    and multiply by the same thing or plus

    something and minus the same thing something and minus the same thing something
    and minus the same thing

    that''s basically it okay and Jensen''s that''s basically it okay and Jensen''s
    that''s basically it okay and Jensen''s

    inequality I guess inequality I guess inequality I guess

    okay so the third thing uh the third the okay so the third thing uh the third
    the okay so the third thing uh the third the

    gener model that we''re going to talk gener model that we''re going to talk gener
    model that we''re going to talk

    about today. It''s called uh Catch Me If'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 71
  start_sec: 3351.67
  end_sec: 3387.27
  text: 'about today. It''s called uh Catch Me If about today. It''s called uh Catch
    Me If

    You Can. Uh basically, I don''t know if You Can. Uh basically, I don''t know if
    You Can. Uh basically, I don''t know if

    you guys have heard of this movie. Maybe you guys have heard of this movie. Maybe
    you guys have heard of this movie. Maybe

    this is too old for you guys. But this is too old for you guys. But this is too
    old for you guys. But

    anyway, this is a movie from uh Leonard anyway, this is a movie from uh Leonard
    anyway, this is a movie from uh Leonard

    DiCaprio and Tom Hanks in the I actually DiCaprio and Tom Hanks in the I actually
    DiCaprio and Tom Hanks in the I actually

    don''t know what what year is it from. don''t know what what year is it from.
    don''t know what what year is it from.

    But anyway, the point is the plot of the But anyway, the point is the plot of
    the But anyway, the point is the plot of the

    movie goes like this, right? Uh so movie goes like this, right? Uh so movie goes
    like this, right? Uh so

    Leonard DiCaprio is like sort of like a Leonard DiCaprio is like sort of like
    a Leonard DiCaprio is like sort of like a

    epic con artist where he just like lie epic con artist where he just like lie
    epic con artist where he just like lie

    about everything in his life. Uh so I about everything in his life. Uh so I about
    everything in his life. Uh so I

    guess the first lie that he made was guess the first lie that he made was guess
    the first lie that he made was

    that he was like a student in class and that he was like a student in class and
    that he was like a student in class and

    he was late or something and then uh he was late or something and then uh he was
    late or something and then uh

    people were laughing at me h and then or people were laughing at me h and then
    or people were laughing at me h and then or

    he was wearing a suit or something like'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 72
  start_sec: 3387.27
  end_sec: 3428.4
  text: 'he was wearing a suit or something like he was wearing a suit or something
    like

    that and people were laughing me hah and that and people were laughing me hah
    and that and people were laughing me hah and

    then he''d be like haha I''m actually your then he''d be like haha I''m actually
    your then he''d be like haha I''m actually your

    substitute teacher and then everyone got substitute teacher and then everyone
    got substitute teacher and then everyone got

    scared well while he was just a student scared well while he was just a student
    scared well while he was just a student

    substitute is student as a teacher substitute is student as a teacher substitute
    is student as a teacher

    anyway uh not important and then Tom anyway uh not important and then Tom anyway
    uh not important and then Tom

    Hanks uh is a FBI detective and Hanks uh is a FBI detective and Hanks uh is a
    FBI detective and

    basically this uh con artist that the basically this uh con artist that the basically
    this uh con artist that the

    Leonardo DiCaprio is is just like Leonardo DiCaprio is is just like Leonardo DiCaprio
    is is just like

    getting like he''s just like getting getting like he''s just like getting getting
    like he''s just like getting

    better and better at making you know better and better at making you know better
    and better at making you know

    lies that he ended up just like making lies that he ended up just like making
    lies that he ended up just like making

    like fake checks or something like that like fake checks or something like that
    like fake checks or something like that

    that raised the attention to the FBI that raised the attention to the FBI that
    raised the attention to the FBI

    detective and then the FDBI detective detective and then the FDBI detective detective
    and then the FDBI detective

    like who is this guy let me try to catch like who is this guy let me try to catch
    like who is this guy let me try to catch

    him and he''s like trying to catch him him and he''s like trying to catch him
    him and he''s like trying to catch him

    but because he''s getting like really but because he''s getting like really'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 73
  start_sec: 3428.4
  end_sec: 3465.28
  text: 'but because he''s getting like really

    good at like faking things so he''s able good at like faking things so he''s able
    good at like faking things so he''s able

    to like fool the detective in into to like fool the detective in into to like
    fool the detective in into

    thinking that he''s not lying and then so thinking that he''s not lying and then
    so thinking that he''s not lying and then so

    he''s able to escape and then the he''s able to escape and then the he''s able
    to escape and then the

    detective be like Oh, wait a minute. detective be like Oh, wait a minute. detective
    be like Oh, wait a minute.

    Wait, wait. He was lying. So the decaf Wait, wait. He was lying. So the decaf
    Wait, wait. He was lying. So the decaf

    get good as well. And then so basically get good as well. And then so basically
    get good as well. And then so basically

    there was a circle where like there''s a there was a circle where like there''s
    a there was a circle where like there''s a

    cycle where the the you know Leonard cycle where the the you know Leonard cycle
    where the the you know Leonard

    DiCaprio gets better and better at like DiCaprio gets better and better at like
    DiCaprio gets better and better at like

    making lies. Uh and Tom Hanks get better making lies. Uh and Tom Hanks get better
    making lies. Uh and Tom Hanks get better

    and better at detecting the lies that and better at detecting the lies that and
    better at detecting the lies that

    Leonard Dapro made. Uh so this is Leonard Dapro made. Uh so this is Leonard Dapro
    made. Uh so this is

    basically while they''re at this like uh basically while they''re at this like
    uh basically while they''re at this like uh

    you know catch me if you can game. Um so you know catch me if you can game. Um
    so you know catch me if you can game. Um so

    this is basically the idea of this is basically the idea of this is basically
    the idea of

    uh the model that we''re going to be uh the model that we''re going to be'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 74
  start_sec: 3465.28
  end_sec: 3508.559
  text: 'uh the model that we''re going to be

    talking about. So you have a generator talking about. So you have a generator
    talking about. So you have a generator

    uh and then you have a discriminator. uh and then you have a discriminator. uh
    and then you have a discriminator.

    The generator is going to try to make The generator is going to try to make The
    generator is going to try to make

    fake samples or generate samples that fake samples or generate samples that fake
    samples or generate samples that

    are more and more realistic so that it are more and more realistic so that it
    are more and more realistic so that it

    can fool the discriminator and the can fool the discriminator and the can fool
    the discriminator and the

    discriminator is trying to get better discriminator is trying to get better discriminator
    is trying to get better

    and better at distinguishing the fake and better at distinguishing the fake and
    better at distinguishing the fake

    samples from the real one. And then you samples from the real one. And then you
    samples from the real one. And then you

    just kind of go on cycles like this. Uh just kind of go on cycles like this. Uh
    just kind of go on cycles like this. Uh

    so and at the end of the day hopefully so and at the end of the day hopefully
    so and at the end of the day hopefully

    the generator is going to be able to the generator is going to be able to the
    generator is going to be able to

    make the some samples that are so make the some samples that are so make the some
    samples that are so

    realistic that is like undistinguishable realistic that is like undistinguishable
    realistic that is like undistinguishable

    uh from human eyes uh that whether or uh from human eyes uh that whether or uh
    from human eyes uh that whether or

    not it''s fake or not. Uh so this thing not it''s fake or not. Uh so this thing
    not it''s fake or not. Uh so this thing

    is called generated average serial is called generated average serial is called
    generated average serial

    network or GAN. Uh this was also network or GAN. Uh this was also'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 75
  start_sec: 3508.559
  end_sec: 3542.64
  text: 'network or GAN. Uh this was also

    developed in I guess 2014. So you see developed in I guess 2014. So you see developed
    in I guess 2014. So you see

    how like a decade ago I don''t know how like a decade ago I don''t know how like
    a decade ago I don''t know

    people just build diff you know like people just build diff you know like people
    just build diff you know like

    they just like so creative. I remember they just like so creative. I remember
    they just like so creative. I remember

    when I was like first like reading this when I was like first like reading this
    when I was like first like reading this

    paper I was like oh my god like what paper I was like oh my god like what paper
    I was like oh my god like what

    what what is going like why how could what what is going like why how could what
    what is going like why how could

    people think of this like just like yeah people think of this like just like yeah
    people think of this like just like yeah

    this just like you know how like when this just like you know how like when this
    just like you know how like when

    you like play video games and you try to you like play video games and you try
    to you like play video games and you try to

    and you be like oh my god I wish I like and you be like oh my god I wish I like
    and you be like oh my god I wish I like

    lost my memory and play again. This is lost my memory and play again. This is
    lost my memory and play again. This is

    how I feel about this paper. This is how I feel about this paper. This is how
    I feel about this paper. This is

    like so good. Uh but basically what''s like so good. Uh but basically what''s
    like so good. Uh but basically what''s

    happening in this paper is that uh you happening in this paper is that uh you
    happening in this paper is that uh you

    first just like sample something um from first just like sample something um from'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 76
  start_sec: 3542.64
  end_sec: 3588.88
  text: 'first just like sample something um from

    a easy to sample distribution such as a easy to sample distribution such as a
    easy to sample distribution such as

    like gausian and then you have a like gausian and then you have a like gausian
    and then you have a

    generator that basically just like generator that basically just like generator
    that basically just like

    forget about all the maximum likelihood forget about all the maximum likelihood
    forget about all the maximum likelihood

    stuff that we just talked about. Forget stuff that we just talked about. Forget
    stuff that we just talked about. Forget

    about all the math. It doesn''t matter about all the math. It doesn''t matter
    about all the math. It doesn''t matter

    anymore. We just the generator this anymore. We just the generator this anymore.
    We just the generator this

    model is going to directly transform model is going to directly transform model
    is going to directly transform

    this sample from this easy to sample this sample from this easy to sample this
    sample from this easy to sample

    distribution because we can directly distribution because we can directly distribution
    because we can directly

    draw a sample from it uh to the draw a sample from it uh to the draw a sample
    from it uh to the

    complicated target distribution like complicated target distribution like complicated
    target distribution like

    image that we want. And then the the image that we want. And then the the image
    that we want. And then the the

    discriminator uh is the only job of the discriminator uh is the only job of the
    discriminator uh is the only job of the

    discriminator is trying to predict uh discriminator is trying to predict uh discriminator
    is trying to predict uh

    whether or not the input to the whether or not the input to the whether or not
    the input to the

    discriminator is a fake image or real discriminator is a fake image or real discriminator
    is a fake image or real

    image and that''s it. And basically this image and that''s it. And basically this
    image and that''s it. And basically this

    what this loss function tells you is what this loss function tells you is what
    this loss function tells you is

    that uh basically this is just a regular that uh basically this is just a regular'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 77
  start_sec: 3588.88
  end_sec: 3659.599
  text: 'that uh basically this is just a regular

    you know classification loss right like you know classification loss right like
    you know classification loss right like

    binary classification law for the for binary classification law for the for binary
    classification law for the for

    the for the discriminator right so the for the discriminator right so the for
    the discriminator right so

    you''re trying to basically you''re trying to basically you''re trying to basically

    the the discriminator is trying to do the the discriminator is trying to do the
    the discriminator is trying to do

    this binary classification well during this binary classification well during
    this binary classification well during

    the training and then the generator is the training and then the generator is
    the training and then the generator is

    trying to like make this binary trying to like make this binary trying to like
    make this binary

    classification classification classification

    classification task as as difficult as classification task as as difficult as
    classification task as as difficult as

    possible. Um so basically this is the possible. Um so basically this is the possible.
    Um so basically this is the

    idea and the the real image are um label idea and the the real image are um label
    idea and the the real image are um label

    by one and then the fake image label by by one and then the fake image label by
    by one and then the fake image label by

    zero. So this is why this is a binary zero. So this is why this is a binary zero.
    So this is why this is a binary

    classification loss. Okay. classification loss. Okay. classification loss. Okay.

    Cool. Any any questions? Yes. >> because uh okay so the the question was >> because
    uh okay so the the question was

    uh he so you understand that why Q of Z uh he so you understand that why Q of
    Z uh he so you understand that why Q of Z

    given X needs to be a probability given X needs to be a probability given X needs
    to be a probability

    because we want to be able to draw because we want to be able to draw because
    we want to be able to draw

    something from it I guess why does the something from it I guess why does the'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 78
  start_sec: 3659.599
  end_sec: 3697.76
  text: 'something from it I guess why does the

    well actually this is not exactly the well actually this is not exactly the well
    actually this is not exactly the

    case we''re going to be talking about how case we''re going to be talking about
    how case we''re going to be talking about how

    VA works uh in details next class uh but VA works uh in details next class uh
    but VA works uh in details next class uh but

    bas basically and then the the question bas basically and then the the question
    bas basically and then the the question

    you''re asking is like why does P of Z you''re asking is like why does P of Z
    you''re asking is like why does P of Z

    given X also needs to be a probability given X also needs to be a probability
    given X also needs to be a probability

    distribution right the answer is we do distribution right the answer is we do
    distribution right the answer is we do

    not have Z right like if we have Z not have Z right like if we have Z not have
    Z right like if we have Z

    already then then we should we''ll be already then then we should we''ll be already
    then then we should we''ll be

    able to learn the encoder and decoder able to learn the encoder and decoder able
    to learn the encoder and decoder

    directly right and the problem is we do directly right and the problem is we do
    directly right and the problem is we do

    not have it and that that just cause a not have it and that that just cause a
    not have it and that that just cause a

    lot of issues which is why we''re kind of lot of issues which is why we''re kind
    of lot of issues which is why we''re kind of

    like using this like proxy loss and like using this like proxy loss and like using
    this like proxy loss and

    we''re not even so this is so basically we''re not even so this is so basically
    we''re not even so this is so basically

    we don''t even have P of Z given X in our we don''t even have P of Z given X in
    our'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 79
  start_sec: 3697.76
  end_sec: 3750.789
  text: 'we don''t even have P of Z given X in our

    final loss. Actually our final loss is final loss. Actually our final loss is
    final loss. Actually our final loss is

    this thing. So our final loss is this this thing. So our final loss is this this
    thing. So our final loss is this

    thing, right? So this thing does thing, right? So this thing does thing, right?
    So this thing does

    actually does not have P of Z given X in actually does not have P of Z given X
    in actually does not have P of Z given X in

    it. And this is just sort of like part it. And this is just sort of like part
    it. And this is just sort of like part

    of our objective that is not actually of our objective that is not actually of
    our objective that is not actually

    trackable and which is why we''re trackable and which is why we''re trackable
    and which is why we''re

    actually uh optimizing the elbow here actually uh optimizing the elbow here actually
    uh optimizing the elbow here

    which does not have Z of uh P of Z given which does not have Z of uh P of Z given
    which does not have Z of uh P of Z given

    X. Yeah, but we''re going to talk about X. Yeah, but we''re going to talk about
    X. Yeah, but we''re going to talk about

    how to do VA properly next class. Okay, how to do VA properly next class. Okay,
    how to do VA properly next class. Okay,

    any other questions? It''s pretty much any other questions? It''s pretty much
    any other questions? It''s pretty much

    the end of class actually. All right. Uh All right. Uh

    so, uh like I said, this is pretty much so, uh like I said, this is pretty much
    so, uh like I said, this is pretty much

    the end of the class. Uh we''re actually the end of the class. Uh we''re actually
    the end of the class. Uh we''re actually

    going to be using all of these going to be using all of these going to be using
    all of these

    techniques that we learned today to techniques that we learned today to techniques
    that we learned today to

    understand how diffusion works. Uh so in'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 80
  start_sec: 3750.789
  end_sec: 3795.48
  text: 'understand how diffusion works. Uh so in understand how diffusion works.
    Uh so in

    uh general next class we''re going to be uh general next class we''re going to
    be uh general next class we''re going to be

    like taking a deeper uh look into uh the like taking a deeper uh look into uh
    the like taking a deeper uh look into uh the

    VA and how to train and sample from one VA and how to train and sample from one
    VA and how to train and sample from one

    and what''s wrong with all of these prior and what''s wrong with all of these
    prior and what''s wrong with all of these prior

    uh uh generic models. The what exactly uh uh generic models. The what exactly
    uh uh generic models. The what exactly

    is diffusion? We''re going to be formally is diffusion? We''re going to be formally
    is diffusion? We''re going to be formally

    talking about diffusion uh next class talking about diffusion uh next class talking
    about diffusion uh next class

    and how was diffusion developed and how was diffusion developed and how was diffusion
    developed

    originally from all of this work originally from all of this work originally from
    all of this work

    especially VAE. This is why we need to especially VAE. This is why we need to
    especially VAE. This is why we need to

    take a deeper look at VAE and also how take a deeper look at VAE and also how
    take a deeper look at VAE and also how

    do people make it work in practice do people make it work in practice do people
    make it work in practice

    actually uh by using the techniques that actually uh by using the techniques that
    actually uh by using the techniques that

    they learn from the prior work. Okay. Uh they learn from the prior work. Okay.
    Uh they learn from the prior work. Okay. Uh

    so that''s the end of class. Make sure to so that''s the end of class. Make sure
    to so that''s the end of class. Make sure to

    join the discord and thanks for coming join the discord and thanks for coming
    join the discord and thanks for coming

    guys. See you.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
---
# CMU 10799 S26: Diffusion & Flow Matching - Lecture 1 - Basics of Probabilistic & Generative Modeling

See the structured chunks above.
