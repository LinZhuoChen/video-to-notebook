---
course_slug: cmu-10799-diffusion-flow
idx: 10
title: 'CMU 10799 S26: Lecture 11 - Guest Lecture Linqi (Alex) Zhou from Luma AI -
  Diffusion & Flow Matching'
video_url: https://www.youtube.com/watch?v=H7MxR3XDt30
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.11
  end_sec: 44.719
  text: 'Cool. Cool. Yeah. Uh and thanks again Cool. Cool. Yeah. Uh and thanks again

    for the invite. Um I''m very excited to for the invite. Um I''m very excited to
    for the invite. Um I''m very excited to

    see you guys. Uh and I hope you''re I see you guys. Uh and I hope you''re I see
    you guys. Uh and I hope you''re I

    hope you are also having a great time hope you are also having a great time hope
    you are also having a great time

    learning about diffusion models. Uh learning about diffusion models. Uh learning
    about diffusion models. Uh

    yeah, I guess uh today I''ll be talking yeah, I guess uh today I''ll be talking
    yeah, I guess uh today I''ll be talking

    about um I mean some I''ll give you some about um I mean some I''ll give you some
    about um I mean some I''ll give you some

    brief overview of the research we did at brief overview of the research we did
    at brief overview of the research we did at

    Luma and the the title of the talk is um Luma and the the title of the talk is
    um Luma and the the title of the talk is um

    towards efficient inference time scaling towards efficient inference time scaling
    towards efficient inference time scaling

    without distillation. And as you may without distillation. And as you may without
    distillation. And as you may

    infer um I''ll be going over a series of infer um I''ll be going over a series
    of infer um I''ll be going over a series of

    efforts uh at at aluma to go beyond efforts uh at at aluma to go beyond efforts
    uh at at aluma to go beyond

    diffusion models trying to design you diffusion models trying to design you diffusion
    models trying to design you

    know new kinds of training frameworks to know new kinds of training frameworks
    to know new kinds of training frameworks to

    directly achieve one or few step directly achieve one or few step directly achieve
    one or few step

    sampling sampling sampling

    and uh all of these works could not be and uh all of these works could not be
    and uh all of these works could not be

    done without my fantastic colleagues at done without my fantastic colleagues at'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 1
  start_sec: 44.719
  end_sec: 96.87
  text: 'done without my fantastic colleagues at

    luma. Yeah. luma. Yeah. luma. Yeah.

    So um in the past five years or so uh So um in the past five years or so uh So
    um in the past five years or so uh

    diffusion models and flow matching have diffusion models and flow matching have
    diffusion models and flow matching have

    kind of dominated the visual generative kind of dominated the visual generative
    kind of dominated the visual generative

    AI landscape and it it it has given rise AI landscape and it it it has given rise
    AI landscape and it it it has given rise

    to these extremely powerful textto image to these extremely powerful textto image
    to these extremely powerful textto image

    and text to video models. Um and here we and text to video models. Um and here
    we and text to video models. Um and here we

    show some samples from some some of the show some samples from some some of the
    show some samples from some some of the

    most notable text conditioned image most notable text conditioned image most notable
    text conditioned image

    models such as uh GB40 image, nano models such as uh GB40 image, nano models such
    as uh GB40 image, nano

    banana, mid journey and flux. Um which banana, mid journey and flux. Um which
    banana, mid journey and flux. Um which

    can now you know produce very can now you know produce very can now you know produce
    very

    semantically meaningful content while semantically meaningful content while semantically
    meaningful content while

    maintaining extreme visual realism. maintaining extreme visual realism. maintaining
    extreme visual realism.

    And at Luma we also train large scale And at Luma we also train large scale And
    at Luma we also train large scale

    text to video models that excel at text to video models that excel at text to
    video models that excel at

    realism. Uh and here we we we also show realism. Uh and here we we we also show
    realism. Uh and here we we we also show

    show some samples. Oh. Oh, I think the show some samples. Oh. Oh, I think the
    show some samples. Oh. Oh, I think the

    videos are not being played correctly. videos are not being played correctly.
    videos are not being played correctly.

    Yeah, there''s some jitter. But um yeah,'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 2
  start_sec: 96.87
  end_sec: 146.39
  text: 'Yeah, there''s some jitter. But um yeah, Yeah, there''s some jitter. But
    um yeah,

    we we show some samples from our latest we we show some samples from our latest
    we we show some samples from our latest

    video model R3. And as you can see that video model R3. And as you can see that
    video model R3. And as you can see that

    these models are very good at generating these models are very good at generating
    these models are very good at generating

    motion and realistic character motion and realistic character motion and realistic
    character

    animation. animation. animation.

    And you know uh behind pretty much all And you know uh behind pretty much all
    And you know uh behind pretty much all

    of these texttovideo models on the of these texttovideo models on the of these
    texttovideo models on the

    market right now uh are the are the are market right now uh are the are the are
    market right now uh are the are the are

    the techniques uh that you have learned the techniques uh that you have learned
    the techniques uh that you have learned

    uh namely diffusion models and flow uh namely diffusion models and flow uh namely
    diffusion models and flow

    matching. matching. matching.

    And And And

    so why why have uh diffusion models so why why have uh diffusion models so why
    why have uh diffusion models

    become the default method right for become the default method right for become
    the default method right for

    visual generation and why are they such visual generation and why are they such
    visual generation and why are they such

    a good method? uh so to understand it a good method? uh so to understand it a
    good method? uh so to understand it

    let''s let''s first look at uh this let''s let''s first look at uh this let''s
    let''s first look at uh this

    animation of a stocastic process defined animation of a stocastic process defined
    animation of a stocastic process defined

    by gausian diffusion which take a by gausian diffusion which take a by gausian
    diffusion which take a

    complex data distribution and transforms complex data distribution and transforms
    complex data distribution and transforms

    it to a simple gausian distribution it to a simple gausian distribution it to
    a simple gausian distribution

    uh so to visualize this process you know'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 3
  start_sec: 146.39
  end_sec: 201.589
  text: 'uh so to visualize this process you know uh so to visualize this process
    you know

    on a on a simple 2D graph um we show on a on a simple 2D graph um we show on a
    on a simple 2D graph um we show

    that here uh say on on the left we have that here uh say on on the left we have
    that here uh say on on the left we have

    u data points from samples from from our u data points from samples from from
    our u data points from samples from from our

    data distribution and on the right we data distribution and on the right we data
    distribution and on the right we

    have samples from a prior distribution have samples from a prior distribution
    have samples from a prior distribution

    and we use these two two simple and we use these two two simple and we use these
    two two simple

    distribution for simplicity. Um and distribution for simplicity. Um and distribution
    for simplicity. Um and

    given a full matching interpolation given a full matching interpolation given
    a full matching interpolation

    between these two distributions uh there between these two distributions uh there
    between these two distributions uh there

    exists a ground truth velocity field. exists a ground truth velocity field. exists
    a ground truth velocity field.

    All right. Uh I I hope you guys have All right. Uh I I hope you guys have All
    right. Uh I I hope you guys have

    covered this. Um there exists a ground covered this. Um there exists a ground
    covered this. Um there exists a ground

    truth velocity field um uh which are truth velocity field um uh which are truth
    velocity field um uh which are

    shown in these uh red vectors and and shown in these uh red vectors and and shown
    in these uh red vectors and and

    there exists a ordinary differential there exists a ordinary differential there
    exists a ordinary differential

    equation uh trajectory that connect one equation uh trajectory that connect one
    equation uh trajectory that connect one

    point from the pi distribution to a point from the pi distribution to a point
    from the pi distribution to a

    point to the data data distribution. point to the data data distribution. point
    to the data data distribution.

    And these trajectories can be seen as'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 4
  start_sec: 201.589
  end_sec: 253.439
  text: 'And these trajectories can be seen as And these trajectories can be seen
    as

    these uh blue lines uh here. And the these uh blue lines uh here. And the these
    uh blue lines uh here. And the

    ground truth of velocity field exists ground truth of velocity field exists ground
    truth of velocity field exists

    but but this is often not known in in but but this is often not known in in but
    but this is often not known in in

    closed form. Uh and that is especially closed form. Uh and that is especially
    closed form. Uh and that is especially

    true for highly complex data true for highly complex data true for highly complex
    data

    distributions like images. Um and the distributions like images. Um and the distributions
    like images. Um and the

    job of diffusion models uh and flow job of diffusion models uh and flow job of
    diffusion models uh and flow

    matching is to learn this uh this this matching is to learn this uh this this
    matching is to learn this uh this this

    velocity field uh with a neuronet velocity field uh with a neuronet velocity field
    uh with a neuronet

    network and and you know these these network and and you know these these network
    and and you know these these

    velocity vectors are also the tangent velocity vectors are also the tangent velocity
    vectors are also the tangent

    vectors uh to these OD trajectories. So vectors uh to these OD trajectories. So
    vectors uh to these OD trajectories. So

    that at inference time uh you can that at inference time uh you can that at inference
    time uh you can

    manually solve an OD starting starting manually solve an OD starting starting
    manually solve an OD starting starting

    from the prior to uh to to go from prior from the prior to uh to to go from prior
    from the prior to uh to to go from prior

    to your data distribution uh following to your data distribution uh following
    to your data distribution uh following

    following the velocity produced by your following the velocity produced by your
    following the velocity produced by your

    neuronet network neuronet network neuronet network

    and uh ultimately the loss comes down to and uh ultimately the loss comes down
    to'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 5
  start_sec: 253.439
  end_sec: 310.639
  text: 'and uh ultimately the loss comes down to

    a simple L2 loss uh which is extremely a simple L2 loss uh which is extremely
    a simple L2 loss uh which is extremely

    stable and very scalable to large number stable and very scalable to large number
    stable and very scalable to large number

    of parameters. But although diffusion and flow matching But although diffusion
    and flow matching

    uh can produce high quality samples uh uh can produce high quality samples uh
    uh can produce high quality samples uh

    they they they still have their own they they they still have their own they they
    they still have their own

    problems right so at inference time um problems right so at inference time um
    problems right so at inference time um

    they solve the so-called probability they solve the so-called probability they
    solve the so-called probability

    flow OD flow OD flow OD

    which were the blue which were the blue which were the blue which were the blue
    which were the blue which were the blue

    lines uh that we saw uh in the previous lines uh that we saw uh in the previous
    lines uh that we saw uh in the previous

    slide and and and we show the marginal slide and and and we show the marginal
    slide and and and we show the marginal

    velocity field as UT here velocity field as UT here velocity field as UT here

    and we argue that uh diffusion and flow and we argue that uh diffusion and flow
    and we argue that uh diffusion and flow

    matching are not optimal in utilizing matching are not optimal in utilizing matching
    are not optimal in utilizing

    the network capacity the network capacity the network capacity

    because uh even if your network predicts because uh even if your network predicts
    because uh even if your network predicts

    UT per perfectly at every single point UT per perfectly at every single point
    UT per perfectly at every single point

    you will still need many many steps to you will still need many many steps to
    you will still need many many steps to

    simulate the OD accurately uh and so simulate the OD accurately uh and so simulate
    the OD accurately uh and so

    naturally it suffers from first uh the naturally it suffers from first uh the'
  concept_slugs:
  - latent-diffusion
  - probability-flow-ode
  - video-diffusion
- idx: 6
  start_sec: 310.639
  end_sec: 363.12
  text: 'naturally it suffers from first uh the

    OD simulation error uh and slow OD simulation error uh and slow OD simulation
    error uh and slow

    inference inference inference

    so um so um so um

    so as a result uh diffusion models scale so as a result uh diffusion models scale
    so as a result uh diffusion models scale

    very poorly with inference compute very poorly with inference compute very poorly
    with inference compute

    uh which can be seen uh here in this uh which can be seen uh here in this uh which
    can be seen uh here in this

    figure where on the x-axis when you have figure where on the x-axis when you have
    figure where on the x-axis when you have

    very small number of steps the the very small number of steps the the very small
    number of steps the the

    performance of the of division models is performance of the of division models
    is performance of the of division models is

    very poor very poor very poor

    uh but the performance generally uh but the performance generally uh but the performance
    generally

    increase uh with more number of steps. increase uh with more number of steps.
    increase uh with more number of steps.

    However, um in a more uh ideal case of However, um in a more uh ideal case of
    However, um in a more uh ideal case of

    sorry for for a more ideal model, you sorry for for a more ideal model, you sorry
    for for a more ideal model, you

    know, it should since neuronet networks know, it should since neuronet networks
    know, it should since neuronet networks

    are uh universal function approximators, are uh universal function approximators,
    are uh universal function approximators,

    it should have enough capacity to it should have enough capacity to it should
    have enough capacity to

    directly represent one or few step directly represent one or few step directly
    represent one or few step

    mapping from prior to data. Uh so so we mapping from prior to data. Uh so so we
    mapping from prior to data. Uh so so we

    term this efficient in inference time term this efficient in inference time term
    this efficient in inference time

    scaling and this can be best uh scaling and this can be best uh'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 7
  start_sec: 363.12
  end_sec: 420.24
  text: 'scaling and this can be best uh

    represented by the green line here where represented by the green line here where
    represented by the green line here where

    where you know when you have very few where you know when you have very few where
    you know when you have very few

    few number of steps you your model uh few number of steps you your model uh few
    number of steps you your model uh

    should still perform close to optimal uh should still perform close to optimal
    uh should still perform close to optimal uh

    compared to division models right now. compared to division models right now.
    compared to division models right now.

    Yeah. And Yeah. And Yeah. And

    there there has actually been a large there there has actually been a large there
    there has actually been a large

    amount of effort uh towards efficient amount of effort uh towards efficient amount
    of effort uh towards efficient

    inference time scaling uh for for inference time scaling uh for for inference
    time scaling uh for for

    division models and these efforts division models and these efforts division models
    and these efforts

    generally fall under two categories of generally fall under two categories of
    generally fall under two categories of

    work. Uh the first category is a work. Uh the first category is a work. Uh the
    first category is a

    two-stage training training pipeline two-stage training training pipeline two-stage
    training training pipeline

    that first does diffusion pre-training that first does diffusion pre-training
    that first does diffusion pre-training

    uh with with a second uh stage of step uh with with a second uh stage of step
    uh with with a second uh stage of step

    distillation. distillation. distillation.

    And here I list some of the And here I list some of the And here I list some of
    the

    representative works such as consistency representative works such as consistency
    representative works such as consistency

    distillation uh distribution matching distillation uh distribution matching distillation
    uh distribution matching

    distillation say score identity distillation say score identity distillation say
    score identity

    dillation and and etc. Um but the dillation and and etc. Um but the dillation
    and and etc. Um but the

    problem uh with these types of models is problem uh with these types of models
    is'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 8
  start_sec: 420.24
  end_sec: 475.199
  text: 'problem uh with these types of models is

    that uh first it it can often suffer that uh first it it can often suffer that
    uh first it it can often suffer

    from training instability. For example, from training instability. For example,
    from training instability. For example,

    for DMD um distribution matching for DMD um distribution matching for DMD um distribution
    matching

    distillation, it requires training two distillation, it requires training two
    distillation, it requires training two

    networks and needs uh careful balancing networks and needs uh careful balancing
    networks and needs uh careful balancing

    of the training schedule uh and and of the training schedule uh and and of the
    training schedule uh and and

    trending hyperparameters to achieve the trending hyperparameters to achieve the
    trending hyperparameters to achieve the

    best results. Uh but the worst problem best results. Uh but the worst problem
    best results. Uh but the worst problem

    in my opinion uh is the added complexity in my opinion uh is the added complexity
    in my opinion uh is the added complexity

    to the training pipeline. So in a real to the training pipeline. So in a real
    to the training pipeline. So in a real

    production setting um we we usually production setting um we we usually production
    setting um we we usually

    train a good base model and train train a good base model and train train a good
    base model and train

    different subm modules for for different different subm modules for for different
    different subm modules for for different

    tasks right so for example after tasks right so for example after tasks right
    so for example after

    training a good text to video model uh training a good text to video model uh
    training a good text to video model uh

    we usually need to train task specific we usually need to train task specific
    we usually need to train task specific

    modules for different tasks such as like modules for different tasks such as like
    modules for different tasks such as like

    uh video editing image to video task and uh video editing image to video task
    and uh video editing image to video task and

    character reference tasks and for all character reference tasks and for all character
    reference tasks and for all

    these different tasks we need to do step these different tasks we need to do step'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 9
  start_sec: 475.199
  end_sec: 523.919
  text: 'these different tasks we need to do step

    step distillation Um and this usually step distillation Um and this usually step
    distillation Um and this usually

    comes after the RL or preference or comes after the RL or preference or comes
    after the RL or preference or

    preference finetuning stages. So this preference finetuning stages. So this preference
    finetuning stages. So this

    just adds a lot of uh complexities to just adds a lot of uh complexities to just
    adds a lot of uh complexities to

    the to to the training pipeline which the to to the training pipeline which the
    to to the training pipeline which

    can cost a lot of you know compute and can cost a lot of you know compute and
    can cost a lot of you know compute and

    and tuning efforts. Um so so another and tuning efforts. Um so so another and
    tuning efforts. Um so so another

    school of thought um is to rethink the school of thought um is to rethink the
    school of thought um is to rethink the

    the pre-training pipeline altogether uh the pre-training pipeline altogether uh
    the pre-training pipeline altogether uh

    to directly achieve one or few step to directly achieve one or few step to directly
    achieve one or few step

    sampling sampling

    and this can avoid a lot of uh the and this can avoid a lot of uh the and this
    can avoid a lot of uh the

    complexities that that came with the complexities that that came with the complexities
    that that came with the

    first uh category. Uh yeah and in the first uh category. Uh yeah and in the first
    uh category. Uh yeah and in the

    second category uh I''ll list some of the second category uh I''ll list some of
    the second category uh I''ll list some of the

    uh representative works such as uh representative works such as uh representative
    works such as

    consistency training uh mean flow uh I''m consistency training uh mean flow uh
    I''m consistency training uh mean flow uh I''m

    sure you guys have have heard about and sure you guys have have heard about and
    sure you guys have have heard about and

    today I''ll be cover two works that we today I''ll be cover two works that we'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 10
  start_sec: 523.919
  end_sec: 576.48
  text: 'today I''ll be cover two works that we

    did at luma uh which is inductive moment did at luma uh which is inductive moment
    did at luma uh which is inductive moment

    matching uh and terminal velocity matching uh and terminal velocity matching uh
    and terminal velocity

    matching. So yeah, so for this talk uh matching. So yeah, so for this talk uh
    matching. So yeah, so for this talk uh

    I''ll I''ll be going over these two works. I''ll I''ll be going over these two
    works. I''ll I''ll be going over these two works.

    Uh yeah, so how do we uh go about Uh yeah, so how do we uh go about Uh yeah, so
    how do we uh go about

    designing our pre-training algorithms designing our pre-training algorithms designing
    our pre-training algorithms

    you know to uh to directly achieve you know to uh to directly achieve you know
    to uh to directly achieve

    efficient inference time scaling? Uh I I efficient inference time scaling? Uh
    I I efficient inference time scaling? Uh I I

    like to think about this problem from like to think about this problem from like
    to think about this problem from

    from from these three deterata uh where from from these three deterata uh where
    from from these three deterata uh where

    we want our model to achieve efficient we want our model to achieve efficient
    we want our model to achieve efficient

    inference uh stable training and high inference uh stable training and high inference
    uh stable training and high

    quality samples all at once. quality samples all at once. quality samples all
    at once.

    Um which means that our model should Um which means that our model should Um which
    means that our model should

    ideally you know lie in the intersection ideally you know lie in the intersection
    ideally you know lie in the intersection

    of these three circles of these three circles of these three circles

    and let let''s now uh try to tackle these and let let''s now uh try to tackle
    these and let let''s now uh try to tackle these

    three challenges one by one. Um yeah and three challenges one by one. Um yeah
    and three challenges one by one. Um yeah and

    yeah let''s first look at uh how we can yeah let''s first look at uh how we can'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 11
  start_sec: 576.48
  end_sec: 635.68
  text: 'yeah let''s first look at uh how we can

    achieve efficient inference by design. So to think about efficient inference uh
    So to think about efficient inference uh

    we we first need to look at what makes we we first need to look at what makes
    we we first need to look at what makes

    diffusion inference slow right let''s diffusion inference slow right let''s diffusion
    inference slow right let''s

    first recall that our diffusion model first recall that our diffusion model first
    recall that our diffusion model

    essentially solves an OD at inference essentially solves an OD at inference essentially
    solves an OD at inference

    time which requires the inference loop time which requires the inference loop
    time which requires the inference loop

    to take uh infinite decimal jumps. uh to take uh infinite decimal jumps. uh to
    take uh infinite decimal jumps. uh

    but uh what we actually want for for one but uh what we actually want for for
    one but uh what we actually want for for one

    or few step generation is is that we or few step generation is is that we or few
    step generation is is that we

    want our model to be able to perform want our model to be able to perform want
    our model to be able to perform

    large jump in time instead of infinite large jump in time instead of infinite
    large jump in time instead of infinite

    decimal jumps right so let''s look at um decimal jumps right so let''s look at
    um decimal jumps right so let''s look at um

    DDIM uh as the most popular sampler for DDIM uh as the most popular sampler for
    DDIM uh as the most popular sampler for

    for division models um which reduced to for division models um which reduced to
    for division models um which reduced to

    oiler sampler in uh inflow matching oiler sampler in uh inflow matching oiler
    sampler in uh inflow matching

    schedule and it takes the following form schedule and it takes the following form
    schedule and it takes the following form

    so uh here here uhat is the output of so uh here here uhat is the output of so
    uh here here uhat is the output of

    your neuronet network taking in XT&T. your neuronet network taking in XT&T.'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 12
  start_sec: 635.68
  end_sec: 694.24
  text: 'your neuronet network taking in XT&T.

    And the result the the result of one And the result the the result of one And
    the result the the result of one

    step DDIM uh at time S can be best step DDIM uh at time S can be best step DDIM
    uh at time S can be best

    visualized in in this uh figure here visualized in in this uh figure here visualized
    in in this uh figure here

    where on the uh on the left we have uh where on the uh on the left we have uh
    where on the uh on the left we have uh

    our data distribution and on the right our data distribution and on the right
    our data distribution and on the right

    we have our prior distribution and the we have our prior distribution and the
    we have our prior distribution and the

    dotted lines are the OD flows the ground dotted lines are the OD flows the ground
    dotted lines are the OD flows the ground

    truth OD. Um so given an initial point truth OD. Um so given an initial point
    truth OD. Um so given an initial point

    xt our onestep ddim is basically an xt our onestep ddim is basically an xt our
    onestep ddim is basically an

    interpolation interpolation interpolation

    uh between the initial point and your uh between the initial point and your uh
    between the initial point and your

    model predicted uh point. model predicted uh point. model predicted uh point.

    So as you can see uh the result XS is is So as you can see uh the result XS is
    is So as you can see uh the result XS is is

    just a linear uh interpolation along just a linear uh interpolation along just
    a linear uh interpolation along

    this line and this means that uh naive this line and this means that uh naive
    this line and this means that uh naive

    DDIM is se is actually severely limited DDIM is se is actually severely limited
    DDIM is se is actually severely limited

    in representing any function of S that''s in representing any function of S that''s
    in representing any function of S that''s

    more more complex than just linear more more complex than just linear more more
    complex than just linear

    relationship. relationship.'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 13
  start_sec: 694.24
  end_sec: 752.48
  text: 'relationship.

    Um so we we I I I like to term ter term Um so we we I I I like to term ter term
    Um so we we I I I like to term ter term

    this the capacity problem uh of DDIM. this the capacity problem uh of DDIM. this
    the capacity problem uh of DDIM.

    So how um so a a simple fix uh for this So how um so a a simple fix uh for this
    So how um so a a simple fix uh for this

    capacity issue is just to inject S into capacity issue is just to inject S into
    capacity issue is just to inject S into

    the network right because neuronet the network right because neuronet the network
    right because neuronet

    networks are universal function networks are universal function networks are universal
    function

    approximators. you know a single call of approximators. you know a single call
    of approximators. you know a single call of

    DDIM if you inject both T and S into the DDIM if you inject both T and S into
    the DDIM if you inject both T and S into the

    into the network a single call of DDIM into the network a single call of DDIM
    into the network a single call of DDIM

    can now cover uh pretty complex can now cover uh pretty complex can now cover
    uh pretty complex

    solutions such as uh OD integrals uh solutions such as uh OD integrals uh solutions
    such as uh OD integrals uh

    which can be visualized here. So before which can be visualized here. So before
    which can be visualized here. So before

    you know the end points uh it it it used you know the end points uh it it it used
    you know the end points uh it it it used

    to be a fixed linear interpolation to be a fixed linear interpolation to be a
    fixed linear interpolation

    uh but now you know uh the endpoint can uh but now you know uh the endpoint can
    uh but now you know uh the endpoint can

    actually slide along this OD integral. actually slide along this OD integral.
    actually slide along this OD integral.

    So so that comes with the power that''s So so that comes with the power that''s'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 14
  start_sec: 752.48
  end_sec: 814.32
  text: 'So so that comes with the power that''s

    uh that''s from the um the neuronet uh that''s from the um the neuronet uh that''s
    from the um the neuronet

    network that that''s being injected with network that that''s being injected with
    network that that''s being injected with

    uh both TNS. uh both TNS. uh both TNS.

    So um yeah to just to recap to speed up So um yeah to just to recap to speed up
    So um yeah to just to recap to speed up

    sampling we simply can inject both TNS sampling we simply can inject both TNS
    sampling we simply can inject both TNS

    into the neural network to increase its into the neural network to increase its
    into the neural network to increase its

    um the the network um the the network um the the network

    capacity uh so that it can perform large capacity uh so that it can perform large
    capacity uh so that it can perform large

    jumping time and this can potentially jumping time and this can potentially jumping
    time and this can potentially

    speed up uh our sample. Okay. Now uh we have resolved the Okay. Now uh we have
    resolved the

    efficiency inference uh uh the the if efficiency inference uh uh the the if efficiency
    inference uh uh the the if

    efficient inference uh by by design. Um efficient inference uh by by design. Um
    efficient inference uh by by design. Um

    let''s now look at how we can tackle the let''s now look at how we can tackle
    the let''s now look at how we can tackle the

    training training stability. Um training training stability. Um training training
    stability. Um

    >> uh hold on Alex Alex um like have people >> uh hold on Alex Alex um like have
    people >> uh hold on Alex Alex um like have people

    been asking questions? I was trying to been asking questions? I was trying to
    been asking questions? I was trying to

    resolve the pizza issue. So are people resolve the pizza issue. So are people
    resolve the pizza issue. So are people

    asking questions? asking questions? asking questions?

    >> I I cannot tell. >> I I cannot tell. >> I I cannot tell.

    >> Okay. Do you guys have questions >> Okay. Do you guys have questions'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 15
  start_sec: 814.32
  end_sec: 852.949
  text: '>> Okay. Do you guys have questions

    regarding the first part? regarding the first part? regarding the first part?

    >> No >> No >> No

    question. question. question.

    >> Okay. Okay. Yeah. Like I I I told Alex >> Okay. Okay. Yeah. Like I I I told
    Alex >> Okay. Okay. Yeah. Like I I I told Alex

    that you guys can ask questions. So you that you guys can ask questions. So you
    that you guys can ask questions. So you

    guys can feel free to ask questions just guys can feel free to ask questions just
    guys can feel free to ask questions just

    like when I''m doing question. Okay. Go like when I''m doing question. Okay. Go
    like when I''m doing question. Okay. Go

    on. on. on.

    >> Yeah. Uh so so for for me the uh the >> Yeah. Uh so so for for me the uh the
    >> Yeah. Uh so so for for me the uh the

    screen is kind of small. Uh so I so I screen is kind of small. Uh so I so I screen
    is kind of small. Uh so I so I

    cannot really see through the camera uh cannot really see through the camera uh
    cannot really see through the camera uh

    if you raised your hand or not. So if if you raised your hand or not. So if if
    you raised your hand or not. So if

    you want to ask questions, I guess you you want to ask questions, I guess you
    you want to ask questions, I guess you

    can just uh like shout or or ask Kelly can just uh like shout or or ask Kelly
    can just uh like shout or or ask Kelly

    to ask questions. Uh yeah. to ask questions. Uh yeah. to ask questions. Uh yeah.

    >> Yes. >> Yes. >> Yes.

    >> Yeah, sure. Go ahead. >> Yeah, sure. Go ahead. >> Yeah, sure. Go ahead.

    >> Yeah. Hi Alex. So in the previous slide, >> Yeah. Hi Alex. So in the previous
    slide, >> Yeah. Hi Alex. So in the previous slide,

    you said that if we also condition the you said that if we also condition the
    you said that if we also condition the

    model on S then we can like s like hope'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 16
  start_sec: 852.949
  end_sec: 903.279
  text: 'model on S then we can like s like hope model on S then we can like s like
    hope

    that it learns the OD better. that it learns the OD better. that it learns the
    OD better.

    >> So what about let''s say uh using like a >> So what about let''s say uh using
    like a >> So what about let''s say uh using like a

    physics informed neural network for the physics informed neural network for the
    physics informed neural network for the

    backbone of the model itself. Would that backbone of the model itself. Would that
    backbone of the model itself. Would that

    like help? like help? like help?

    uh it depends on so for physics informed uh it depends on so for physics informed
    uh it depends on so for physics informed

    neural network uh it to my understanding neural network uh it to my understanding
    neural network uh it to my understanding

    it it it still solves the OD uh at it it it still solves the OD uh at it it it
    still solves the OD uh at

    inference right so that that in itself inference right so that that in itself
    inference right so that that in itself

    is still it''s still a diffusion model uh is still it''s still a diffusion model
    uh is still it''s still a diffusion model uh

    by design here what we want to by design here what we want to by design here what
    we want to

    parameterize is for the model to have parameterize is for the model to have parameterize
    is for the model to have

    enough capacity to directly with one enough capacity to directly with one enough
    capacity to directly with one

    step uh uh can represent a large jump in step uh uh can represent a large jump
    in step uh uh can represent a large jump in

    time uh that that can cover uh the OD time uh that that can cover uh the OD time
    uh that that can cover uh the OD

    integral. Um so um yeah so to my integral. Um so um yeah so to my integral. Um
    so um yeah so to my

    understanding in the physics inform understanding in the physics inform understanding
    in the physics inform

    neural network you are still trying to neural network you are still trying to'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 17
  start_sec: 903.279
  end_sec: 960.079
  text: 'neural network you are still trying to

    fit the tangent velocity at every single fit the tangent velocity at every single
    fit the tangent velocity at every single

    point. >> I hope that answers the question. >> I hope that answers the question.

    >> Yeah. >> Yeah. >> Yeah.

    >> Cool. >> Cool. >> Cool.

    Cool. Okay. Uh yeah. So uh yeah let''s Cool. Okay. Uh yeah. So uh yeah let''s
    Cool. Okay. Uh yeah. So uh yeah let''s

    look at uh the second challenge. um how look at uh the second challenge. um how
    look at uh the second challenge. um how

    do we design a a good uh a pre-training do we design a a good uh a pre-training
    do we design a a good uh a pre-training

    algorithm um you know by uh you know how algorithm um you know by uh you know
    how algorithm um you know by uh you know how

    how do we design a good pre-training how do we design a good pre-training how
    do we design a good pre-training

    algorithm and uh here I want to cover algorithm and uh here I want to cover algorithm
    and uh here I want to cover

    two approaches that we did uh right one two approaches that we did uh right one
    two approaches that we did uh right one

    one is inductive moment matching and the one is inductive moment matching and
    the one is inductive moment matching and the

    other one is terminal velocity matching other one is terminal velocity matching
    other one is terminal velocity matching

    and let''s uh now first look at uh the and let''s uh now first look at uh the
    and let''s uh now first look at uh the

    first approach first approach first approach

    oh yeah and and both and just reminder oh yeah and and both and just reminder
    oh yeah and and both and just reminder

    both both of these both both of these both both of these

    approaches uh try to achieve the same approaches uh try to achieve the same approaches
    uh try to achieve the same

    goal uh that is to train a one-step or goal uh that is to train a one-step or
    goal uh that is to train a one-step or

    few step uh network uh directly from few step uh network uh directly from'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 18
  start_sec: 960.079
  end_sec: 1025.439
  text: 'few step uh network uh directly from

    from scratch. Okay. So the first method uh inductive Okay. So the first method
    uh inductive

    mode matching. So for for this uh for mode matching. So for for this uh for mode
    matching. So for for this uh for

    this paper uh it consists of two major this paper uh it consists of two major
    this paper uh it consists of two major

    components. The first uh being a components. The first uh being a components.
    The first uh being a

    samplebased distribution matching samplebased distribution matching samplebased
    distribution matching

    objective that''s based on maximum mean objective that''s based on maximum mean
    objective that''s based on maximum mean

    discrepancy or short for MMD discrepancy or short for MMD discrepancy or short
    for MMD

    and the second component being the and the second component being the and the
    second component being the

    concept of inductive learning which we concept of inductive learning which we
    concept of inductive learning which we

    take inspiration from mathematical take inspiration from mathematical take inspiration
    from mathematical

    induction and I''ll uh talk talk about induction and I''ll uh talk talk about
    induction and I''ll uh talk talk about

    these two components separately uh in these two components separately uh in these
    two components separately uh in

    the following slides. the following slides. the following slides.

    So for the first component um consider So for the first component um consider
    So for the first component um consider

    our data uh and prior distribution right our data uh and prior distribution right
    our data uh and prior distribution right

    uh so say this is the your data uh so say this is the your data uh so say this
    is the your data

    distribution and and this a prior um and distribution and and this a prior um
    and distribution and and this a prior um and

    and and we consider any an interpolation and and we consider any an interpolation
    and and we consider any an interpolation

    between them. So uh the interpolation between them. So uh the interpolation between
    them. So uh the interpolation

    here is given by your your normal flow here is given by your your normal flow
    here is given by your your normal flow

    matching interpolation matching interpolation matching interpolation

    and we call the two intermediate and we call the two intermediate'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 19
  start_sec: 1025.439
  end_sec: 1080.16
  text: 'and we call the two intermediate

    distributions uh QS and QT where where distributions uh QS and QT where where
    distributions uh QS and QT where where

    QS is closer to our data distribution QS is closer to our data distribution QS
    is closer to our data distribution

    than QT. So our goal here is to learn a than QT. So our goal here is to learn
    a than QT. So our goal here is to learn a

    mapping from QT to QS. mapping from QT to QS. mapping from QT to QS.

    uh and to do so well what what we''re uh and to do so well what what we''re uh
    and to do so well what what we''re

    going to do is to we we use the modified going to do is to we we use the modified
    going to do is to we we use the modified

    uh DDIM with two time steps to map our uh DDIM with two time steps to map our
    uh DDIM with two time steps to map our

    uh our marginal distribution QT to some uh our marginal distribution QT to some
    uh our marginal distribution QT to some

    model distribution uh P. And here the model distribution uh P. And here the model
    distribution uh P. And here the

    model distribution is indexed by by an model distribution is indexed by by an
    model distribution is indexed by by an

    end an end time step S and a starting end an end time step S and a starting end
    an end time step S and a starting

    time step T. So so that''s uh the time step T. So so that''s uh the time step
    T. So so that''s uh the

    notation that that that we use. notation that that that we use. notation that
    that that we use.

    Um yeah and and this DDIM uh is a two Um yeah and and this DDIM uh is a two Um
    yeah and and this DDIM uh is a two

    time step uh injected uh as we mentioned time step uh injected uh as we mentioned
    time step uh injected uh as we mentioned

    in the previous slides. in the previous slides. in the previous slides.

    So So So

    to to learn this mapping uh that to to learn this mapping uh that'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 20
  start_sec: 1080.16
  end_sec: 1148.87
  text: 'to to learn this mapping uh that

    transforms QT to QS uh a naive approach transforms QT to QS uh a naive approach
    transforms QT to QS uh a naive approach

    right to learn this mapping uh is is to right to learn this mapping uh is is to
    right to learn this mapping uh is is to

    uh use some proper distribution matching uh use some proper distribution matching
    uh use some proper distribution matching

    objective objective objective

    to to to

    to match this uh distribution to our to match this uh distribution to our to match
    this uh distribution to our

    target distribution QS. target distribution QS. target distribution QS.

    Um Um Um

    and uh for for this work what we use is and uh for for this work what we use is
    and uh for for this work what we use is

    MMD and we use it for its uh training MMD and we use it for its uh training MMD
    and we use it for its uh training

    training stability and you can certainly training stability and you can certainly
    training stability and you can certainly

    use something like GAN uh to match in use something like GAN uh to match in use
    something like GAN uh to match in

    distribution but we wanted to avoid distribution but we wanted to avoid distribution
    but we wanted to avoid

    adversarial training because it''s hard adversarial training because it''s hard
    adversarial training because it''s hard

    uh to scale. So so uh the natural uh to scale. So so uh the natural uh to scale.
    So so uh the natural

    alternative is is u alternative is is u alternative is is u

    uh M&D in this case. Yeah. And uh M&D in this case. Yeah. And uh M&D in this case.
    Yeah. And

    Yeah. Oh yeah. And finally, we want to Yeah. Oh yeah. And finally, we want to
    Yeah. Oh yeah. And finally, we want to

    um you know note that the DD mapping is um you know note that the DD mapping is
    um you know note that the DD mapping is

    is what we ultimately want to learn. And a short note on MMD uh intuitively And
    a short note on MMD uh intuitively

    is it is kind of kind of like a GAN but'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 21
  start_sec: 1148.87
  end_sec: 1212.48
  text: 'is it is kind of kind of like a GAN but is it is kind of kind of like a GAN
    but

    uh the optimal discriminator is already uh the optimal discriminator is already
    uh the optimal discriminator is already

    chosen uh in the reproducing kernel chosen uh in the reproducing kernel chosen
    uh in the reproducing kernel

    cuber space. So there''s no need uh for cuber space. So there''s no need uh for
    cuber space. So there''s no need uh for

    you to train a discriminator uh in a you to train a discriminator uh in a you
    to train a discriminator uh in a

    minimax objective. So there is no minimax objective. So there is no minimax objective.
    So there is no

    adversarial training here. Uh and the adversarial training here. Uh and the adversarial
    training here. Uh and the

    learning is very stable. And as a learning is very stable. And as a learning is
    very stable. And as a

    trade-off, it uses multiple particles trade-off, it uses multiple particles trade-off,
    it uses multiple particles

    for estimating distributions, meaning for estimating distributions, meaning for
    estimating distributions, meaning

    that you''ll need multiple samples uh to that you''ll need multiple samples uh
    to that you''ll need multiple samples uh to

    calculate your MMD objective. calculate your MMD objective. calculate your MMD
    objective.

    And uh standard kernels like uh RBF And uh standard kernels like uh RBF And uh
    standard kernels like uh RBF

    kernel and and the plus kernel they kernel and and the plus kernel they kernel
    and and the plus kernel they

    implicitly match all moments of your implicitly match all moments of your implicitly
    match all moments of your

    distribution. Uh and there''s actually a distribution. Uh and there''s actually
    a distribution. Uh and there''s actually a

    very deep literature that that studies very deep literature that that studies
    very deep literature that that studies

    moment matching as a substitute for moment matching as a substitute for moment
    matching as a substitute for

    maximum likelihood. maximum likelihood. maximum likelihood.

    And and yeah uh for empirical And and yeah uh for empirical And and yeah uh for
    empirical

    implementation we use multiple particles implementation we use multiple particles
    implementation we use multiple particles

    to estimate the MMD expectation. And um a second component uh for IM is'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 22
  start_sec: 1212.48
  end_sec: 1261.12
  text: 'And um a second component uh for IM is

    the concept of inductive learning. Uh so the concept of inductive learning. Uh
    so the concept of inductive learning. Uh so

    consider the same learning scheme where consider the same learning scheme where
    consider the same learning scheme where

    where we transform you know QT with a where we transform you know QT with a where
    we transform you know QT with a

    single call of DDIM with Q time step. uh single call of DDIM with Q time step.
    uh single call of DDIM with Q time step. uh

    and it it can actually be quite and it it can actually be quite and it it can
    actually be quite

    difficult uh for the model to learn the difficult uh for the model to learn the
    difficult uh for the model to learn the

    ground truth QS directly especially when ground truth QS directly especially when
    ground truth QS directly especially when

    when QT is very far away from QS which when QT is very far away from QS which
    when QT is very far away from QS which

    makes our model distribution P theta makes our model distribution P theta makes
    our model distribution P theta

    very far away from from QS now um it is very far away from from QS now um it is
    very far away from from QS now um it is

    a known problem that uh it''s it''s very a known problem that uh it''s it''s very
    a known problem that uh it''s it''s very

    difficult to scale conventional MMD to difficult to scale conventional MMD to
    difficult to scale conventional MMD to

    high dimension because your standard high dimension because your standard high
    dimension because your standard

    kernels are not going to be very kernels are not going to be very kernels are
    not going to be very

    meaningful if the sample are already far meaningful if the sample are already
    far meaningful if the sample are already far

    away from from from each other. So uh so away from from from each other. So uh
    so away from from from each other. So uh so

    that is the case here when QT is very that is the case here when QT is very'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 23
  start_sec: 1261.12
  end_sec: 1318.4
  text: 'that is the case here when QT is very

    far away from from QS. Um so naively far away from from QS. Um so naively far
    away from from QS. Um so naively

    matching these two distributions with matching these two distributions with matching
    these two distributions with

    MMD is going to be very hard. Uh so we MMD is going to be very hard. Uh so we
    MMD is going to be very hard. Uh so we

    will need a way you know to find an will need a way you know to find an will need
    a way you know to find an

    alternative target distribution to match alternative target distribution to match
    alternative target distribution to match

    against in order to to learn P theta. against in order to to learn P theta. against
    in order to to learn P theta.

    So here''s when where induction come So here''s when where induction come So here''s
    when where induction come

    comes in. Um and what we do is to use a comes in. Um and what we do is to use
    a comes in. Um and what we do is to use a

    distribution QR uh that is chosen to be distribution QR uh that is chosen to be
    distribution QR uh that is chosen to be

    very close to QT. So R here is a very close to QT. So R here is a very close to
    QT. So R here is a

    deterministic function of T that is deterministic function of T that is deterministic
    function of T that is

    chosen to be very close to T chosen to be very close to T chosen to be very close
    to T

    and and we use our own model to map QR and and we use our own model to map QR
    and and we use our own model to map QR

    to some model distribution at S. to some model distribution at S. to some model
    distribution at S.

    Right? So, so uh and we can use our Right? So, so uh and we can use our Right?
    So, so uh and we can use our

    inductive assumption that this inductive assumption that this inductive assumption
    that this

    distribution is already very close to distribution is already very close to distribution
    is already very close to

    QQS. QQS.'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 24
  start_sec: 1318.4
  end_sec: 1374.88
  text: 'QQS.

    um and and and learning the model um and and and learning the model um and and
    and learning the model

    learning the model distribution uh learning the model distribution uh learning
    the model distribution uh

    starting from R uh as as as a pseudo starting from R uh as as as a pseudo starting
    from R uh as as as a pseudo

    target to train the model distribution target to train the model distribution
    target to train the model distribution

    from from T is a much easier task uh from from T is a much easier task uh from
    from T is a much easier task uh

    than directly learning the ground truth than directly learning the ground truth
    than directly learning the ground truth

    QS because DDIM is a deterministic QS because DDIM is a deterministic QS because
    DDIM is a deterministic

    transformation and QR and QT which are transformation and QR and QT which are
    transformation and QR and QT which are

    already very close uh when they undergo already very close uh when they undergo
    already very close uh when they undergo

    the same deterministic transformation the same deterministic transformation the
    same deterministic transformation

    the resulting distributions are not the resulting distributions are not the resulting
    distributions are not

    going to be too far away. So this going to be too far away. So this going to be
    too far away. So this

    closeness uh in in these two model closeness uh in in these two model closeness
    uh in in these two model

    distribution allows for meaningful distribution allows for meaningful distribution
    allows for meaningful

    training gradient uh and bypasses some training gradient uh and bypasses some
    training gradient uh and bypasses some

    of the conventional problems of MMD of the conventional problems of MMD of the
    conventional problems of MMD

    and okay and now of course in induction and okay and now of course in induction
    and okay and now of course in induction

    uh there is there''s also the base case uh there is there''s also the base case
    uh there is there''s also the base case

    that we need to satisfy. that we need to satisfy. that we need to satisfy.

    So what is the base case here? The base So what is the base case here? The base'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 25
  start_sec: 1374.88
  end_sec: 1435.27
  text: 'So what is the base case here? The base

    case is if you take QS. case is if you take QS. case is if you take QS.

    Oh uh yeah and here we need to yeah Oh uh yeah and here we need to yeah Oh uh
    yeah and here we need to yeah

    match in MMD. So this task is it it is a match in MMD. So this task is it it is
    a match in MMD. So this task is it it is a

    lot easier than directly learning QS. lot easier than directly learning QS. lot
    easier than directly learning QS.

    So the base case here is we if we take So the base case here is we if we take
    So the base case here is we if we take

    QS as the input to our DDIM and map it QS as the input to our DDIM and map it
    QS as the input to our DDIM and map it

    to the same time step S then you will to the same time step S then you will to
    the same time step S then you will

    get identically uh QS. get identically uh QS. get identically uh QS.

    And what you can visualize uh here is And what you can visualize uh here is And
    what you can visualize uh here is

    that if you slide QR that if you slide QR that if you slide QR

    uh towards QS gradually, uh towards QS gradually, uh towards QS gradually,

    right? The um then then the resulting right? The um then then the resulting right?
    The um then then the resulting

    model distribution here is going to be model distribution here is going to be
    model distribution here is going to be

    closer and closer to QS. So when QR uh closer and closer to QS. So when QR uh
    closer and closer to QS. So when QR uh

    is identically equal to QS, the the is identically equal to QS, the the is identically
    equal to QS, the the

    resulting model distribution is going to resulting model distribution is going
    to resulting model distribution is going to

    be identically equal to QS. And this is be identically equal to QS. And this is
    be identically equal to QS. And this is

    true regardless of your theta and even'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 26
  start_sec: 1435.27
  end_sec: 1493.919
  text: 'true regardless of your theta and even true regardless of your theta and
    even

    when your theta is untrained um that the when your theta is untrained um that
    the when your theta is untrained um that the

    this uh identity mapping is true and this uh identity mapping is true and this
    uh identity mapping is true and

    this is a special property of DDIM. this is a special property of DDIM. this is
    a special property of DDIM.

    So that that constitutes of our base So that that constitutes of our base So that
    that constitutes of our base

    case. case. case.

    So uh for a for an animation of the So uh for a for an animation of the So uh
    for a for an animation of the

    induction um what you can uh understand induction um what you can uh understand
    induction um what you can uh understand

    here is say if you uh take uh QT that is here is say if you uh take uh QT that
    is here is say if you uh take uh QT that is

    very close to uh QS. So t here say is very close to uh QS. So t here say is very
    close to uh QS. So t here say is

    very close to s and you map it to your very close to s and you map it to your
    very close to s and you map it to your

    model distribution uh p p theta model distribution uh p p theta model distribution
    uh p p theta

    when when t is very close to s um when when t is very close to s um when when
    t is very close to s um

    when when t is very clo very close to s when when t is very clo very close to
    s when when t is very clo very close to s

    r is chosen to be identically equal to r is chosen to be identically equal to
    r is chosen to be identically equal to

    s. s. s.

    So your target distribution you know p So your target distribution you know p
    So your target distribution you know p

    theta theta theta

    is going to be the base case itself. So is going to be the base case itself. So'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 27
  start_sec: 1493.919
  end_sec: 1551.52
  text: 'is going to be the base case itself. So

    this is going to be identically equal to this is going to be identically equal
    to this is going to be identically equal to

    QS. QS. QS.

    So what you''re matching against is So what you''re matching against is So what
    you''re matching against is

    actually you''re matching against the actually you''re matching against the actually
    you''re matching against the

    base case. Uh so so this model base case. Uh so so this model base case. Uh so
    so this model

    transformation uh so it it''s it it''s transformation uh so it it''s it it''s
    transformation uh so it it''s it it''s

    much easier for you to learn this uh QQS much easier for you to learn this uh
    QQS much easier for you to learn this uh QQS

    here because QT is very close to QS. So here because QT is very close to QS. So
    here because QT is very close to QS. So

    uh the optimization process is is going uh the optimization process is is going
    uh the optimization process is is going

    to be a lot easier to be a lot easier to be a lot easier

    and And um uh so now we can move QT slightly And um uh so now we can move QT slightly

    far farther away and we do the same far farther away and we do the same far farther
    away and we do the same

    process to map it to some model model process to map it to some model model process
    to map it to some model model

    distribution. distribution. distribution.

    And now instead of using QS as our And now instead of using QS as our And now
    instead of using QS as our

    training target, we we we map uh QR to training target, we we we map uh QR to
    training target, we we we map uh QR to

    some model distribution at at QS at S some model distribution at at QS at S some
    model distribution at at QS at S

    and we use this as our pseudo target to and we use this as our pseudo target to
    and we use this as our pseudo target to

    train our train our train our

    >> question. Yeah, >> question. Yeah,'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 28
  start_sec: 1551.52
  end_sec: 1600.72
  text: '>> question. Yeah,

    >> about the choice of MMD. I mean uh we >> about the choice of MMD. I mean uh
    we >> about the choice of MMD. I mean uh we

    can formalize the the flow matching as can formalize the the flow matching as
    can formalize the the flow matching as

    optimal transport problem and it''s optimal transport problem and it''s optimal
    transport problem and it''s

    natural to use something like sequence natural to use something like sequence
    natural to use something like sequence

    divergence or what''s the distance as a divergence or what''s the distance as
    a divergence or what''s the distance as a

    matrix to measure the distance of the matrix to measure the distance of the matrix
    to measure the distance of the

    two distribution. So why you choose to two distribution. So why you choose to
    two distribution. So why you choose to

    use MMB here? use MMB here? use MMB here?

    >> Oh yeah because uh if you want so >> Oh yeah because uh if you want so >> Oh
    yeah because uh if you want so

    optimizing what''s sign distance is not optimizing what''s sign distance is not
    optimizing what''s sign distance is not

    uh straightforward right? So you for uh straightforward right? So you for uh straightforward
    right? So you for

    high dimensional data you need to rely high dimensional data you need to rely
    high dimensional data you need to rely

    on something like GAN to to optimize for on something like GAN to to optimize
    for on something like GAN to to optimize for

    >> you can''t directly measure the what''s >> you can''t directly measure the
    what''s >> you can''t directly measure the what''s

    distance or simple dish or something distance or simple dish or something distance
    or simple dish or something

    like that like that like that

    >> for for for simp for simple distribution >> for for for simp for simple distribution
    >> for for for simp for simple distribution

    yes it''s uh it''s easy uh but but for yes it''s uh it''s easy uh but but for
    yes it''s uh it''s easy uh but but for

    high dimensional data you you will need high dimensional data you you will need
    high dimensional data you you will need

    some iterative scheme uh to to actually some iterative scheme uh to to actually'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 29
  start_sec: 1600.72
  end_sec: 1651.19
  text: 'some iterative scheme uh to to actually

    optimize uh that objective. So yeah, so optimize uh that objective. So yeah, so
    optimize uh that objective. So yeah, so

    that''s part of the reason that we don''t that''s part of the reason that we don''t
    that''s part of the reason that we don''t

    want to directly measure. Yeah. want to directly measure. Yeah. want to directly
    measure. Yeah.

    >> Yeah. But when you implement the MMP, >> Yeah. But when you implement the MMP,
    >> Yeah. But when you implement the MMP,

    you still need to choose some kind of you still need to choose some kind of you
    still need to choose some kind of

    kernel still with a high dimension data. kernel still with a high dimension data.
    kernel still with a high dimension data.

    For example, if you use a kernel, you For example, if you use a kernel, you For
    example, if you use a kernel, you

    still need to choose like bandwise and I still need to choose like bandwise and
    I still need to choose like bandwise and I

    I think MM is very sensitive to the I think MM is very sensitive to the I think
    MM is very sensitive to the

    choice of bandwise. choice of bandwise. choice of bandwise.

    >> Uh so in in our choice uh so we actually >> Uh so in in our choice uh so we
    actually >> Uh so in in our choice uh so we actually

    just use LLAS kernel in this case. Uh just use LLAS kernel in this case. Uh just
    use LLAS kernel in this case. Uh

    and and because the the samples from QR and and because the the samples from QR
    and and because the the samples from QR

    and samples from QT are are very close and samples from QT are are very close
    and samples from QT are are very close

    to each other, um it actually provides to each other, um it actually provides
    to each other, um it actually provides

    you a pretty good training signal. Uh you a pretty good training signal. Uh you
    a pretty good training signal. Uh

    and and we so the standard kernels like and and we so the standard kernels like
    and and we so the standard kernels like

    RBF and and uh Llas kernel both work in'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 30
  start_sec: 1651.19
  end_sec: 1700.95
  text: 'RBF and and uh Llas kernel both work in RBF and and uh Llas kernel both work
    in

    our case. our case. our case.

    >> Yeah. Yeah. Thank you. >> Yeah. Yeah. Thank you. >> Yeah. Yeah. Thank you.

    >> Yeah. Yeah, that''s a great question. >> Yeah. Yeah, that''s a great question.
    >> Yeah. Yeah, that''s a great question.

    Yeah. Uh yeah, I I guess that also Yeah. Uh yeah, I I guess that also Yeah. Uh
    yeah, I I guess that also

    highlights the need for inductive highlights the need for inductive highlights
    the need for inductive

    learning because if you just do directly learning because if you just do directly
    learning because if you just do directly

    matching it uh with the ground truth QQS matching it uh with the ground truth
    QQS matching it uh with the ground truth QQS

    uh especially when QT is very far away, uh especially when QT is very far away,
    uh especially when QT is very far away,

    it''s uh it it usually doesn''t work. So it''s uh it it usually doesn''t work.
    So it''s uh it it usually doesn''t work. So

    yeah, yeah, yeah,

    cool. Uh yeah, so we''re at this step of cool. Uh yeah, so we''re at this step
    of cool. Uh yeah, so we''re at this step of

    our induction. uh when we use our models our induction. uh when we use our models
    our induction. uh when we use our models

    uh our own model distribution as a uh our own model distribution as a uh our own
    model distribution as a

    pseudo target uh because we have seen on pseudo target uh because we have seen
    on pseudo target uh because we have seen on

    the previous animation that this uh this the previous animation that this uh this
    the previous animation that this uh this

    distribution was already trained to be distribution was already trained to be
    distribution was already trained to be

    uh to be very close to QS already. So uh to be very close to QS already. So uh
    to be very close to QS already. So

    this can now act as your uh your pseudo this can now act as your uh your pseudo
    this can now act as your uh your pseudo

    target to to train the new the new time'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 31
  start_sec: 1700.95
  end_sec: 1751.44
  text: 'target to to train the new the new time target to to train the new the new
    time

    step um the the new model distribution step um the the new model distribution
    step um the the new model distribution

    and yeah so this so this leverages the and yeah so this so this leverages the
    and yeah so this so this leverages the

    inductive assumption and the same thing inductive assumption and the same thing
    inductive assumption and the same thing

    is true here and same thing is true is true here and same thing is true is true
    here and same thing is true

    here. Uh so yeah at the end what you''ll here. Uh so yeah at the end what you''ll
    here. Uh so yeah at the end what you''ll

    be able to get from this is uh you you be able to get from this is uh you you
    be able to get from this is uh you you

    you''ll be able to um you know uh take you''ll be able to um you know uh take
    you''ll be able to um you know uh take

    the private distribution and map it to the private distribution and map it to
    the private distribution and map it to

    any uh to any marginal distribution in any uh to any marginal distribution in
    any uh to any marginal distribution in

    between. between. between.

    So yeah so this is kind of a gist of So yeah so this is kind of a gist of So yeah
    so this is kind of a gist of

    IMM. Um IMM. Um IMM. Um

    and empirically uh we show that our and empirically uh we show that our and empirically
    uh we show that our

    objective is very stable as long as you objective is very stable as long as you
    objective is very stable as long as you

    use more than four particles uh for use more than four particles uh for use more
    than four particles uh for

    estimating MMD. Uh and you can see it in estimating MMD. Uh and you can see it
    in estimating MMD. Uh and you can see it in

    the training comparison here between IMM the training comparison here between
    IMM the training comparison here between IMM

    and improved consensity training uh in and improved consensity training uh in'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 32
  start_sec: 1751.44
  end_sec: 1814.72
  text: 'and improved consensity training uh in

    discrete time. Uh and this is done on discrete time. Uh and this is done on discrete
    time. Uh and this is done on

    imageet. So consensity training imageet. So consensity training imageet. So consensity
    training

    collapses after some some iterations and collapses after some some iterations
    and collapses after some some iterations and

    and you know it''s it''s generally hard to and you know it''s it''s generally
    hard to and you know it''s it''s generally hard to

    tune uh and IMM however remains stable tune uh and IMM however remains stable
    tune uh and IMM however remains stable

    uh throughout the training and experimentally we achieved 1.9 FID and experimentally
    we achieved 1.9 FID

    with eight steps uh and 1.90 FID with 16 with eight steps uh and 1.90 FID with
    16 with eight steps uh and 1.90 FID with 16

    steps and this is this was a notable steps and this is this was a notable steps
    and this is this was a notable

    improvement over diffusion models and improvement over diffusion models and improvement
    over diffusion models and

    flow matching baseline and some of the flow matching baseline and some of the
    flow matching baseline and some of the

    other auto reggressive baselines as other auto reggressive baselines as other
    auto reggressive baselines as

    well. Uh and of course these results well. Uh and of course these results well.
    Uh and of course these results

    have become um obsolete have become um obsolete have become um obsolete

    you know given the recent explosion of you know given the recent explosion of
    you know given the recent explosion of

    one step models. Um but yes uh at the one step models. Um but yes uh at the one
    step models. Um but yes uh at the

    time uh this was the state-of-the-art um time uh this was the state-of-the-art
    um time uh this was the state-of-the-art um

    fewstep model and similar to diffusion um our method and similar to diffusion
    um our method

    also scales with both training and and also scales with both training and and
    also scales with both training and and

    sampling compute as well as uh sampling compute as well as uh sampling compute
    as well as uh

    transformer size. Uh so so so the more transformer size. Uh so so so the more'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 33
  start_sec: 1814.72
  end_sec: 1869.279
  text: 'transformer size. Uh so so so the more

    compute you throw at it, it gets uh compute you throw at it, it gets uh compute
    you throw at it, it gets uh

    better performance in general better performance in general better performance
    in general

    and and this can also be visualized here and and this can also be visualized here
    and and this can also be visualized here

    uh on on these grids where on the x-axis uh on on these grids where on the x-axis
    uh on on these grids where on the x-axis

    uh on the yaxis uh on the yaxis uh on the yaxis

    you have increasing model size and on you have increasing model size and on you
    have increasing model size and on

    the on the x axis you have increasing the on the x axis you have increasing the
    on the x axis you have increasing

    sampling steps. sampling steps. sampling steps.

    Uh and in general what we observe is Uh and in general what we observe is Uh and
    in general what we observe is

    that the more the larger model you throw that the more the larger model you throw
    that the more the larger model you throw

    at it and the more sampling compute you at it and the more sampling compute you
    at it and the more sampling compute you

    spend it it gives you better results and here uh I want to note some and here
    uh I want to note some

    relationships uh between IMM and some relationships uh between IMM and some relationships
    uh between IMM and some

    other prior works as well as some other prior works as well as some other prior
    works as well as some

    recently released papers. Um so the so recently released papers. Um so the so
    recently released papers. Um so the so

    the first work we want to note u is the first work we want to note u is the first
    work we want to note u is

    constancy training. constancy training. constancy training.

    So what we found is that Imm can reduce So what we found is that Imm can reduce
    So what we found is that Imm can reduce

    to consistency training as a special to consistency training as a special'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 34
  start_sec: 1869.279
  end_sec: 1924.63
  text: 'to consistency training as a special

    case if our MMD objective uses only one case if our MMD objective uses only one
    case if our MMD objective uses only one

    particle. Uh and instead of using LLAS particle. Uh and instead of using LLAS
    particle. Uh and instead of using LLAS

    kernel uh consistency training only uses kernel uh consistency training only uses
    kernel uh consistency training only uses

    the L L2 kernel. Uh so if you know MMD the L L2 kernel. Uh so if you know MMD
    the L L2 kernel. Uh so if you know MMD

    uh it can be generally decomposed into uh it can be generally decomposed into
    uh it can be generally decomposed into

    an attraction term and a repulsion term an attraction term and a repulsion term
    an attraction term and a repulsion term

    between particles. So using one particle between particles. So using one particle
    between particles. So using one particle

    basically says okay now you''re going to basically says okay now you''re going
    to basically says okay now you''re going to

    ignore the repulsion term and and only ignore the repulsion term and and only
    ignore the repulsion term and and only

    use the attraction term and this is use the attraction term and this is use the
    attraction term and this is

    actually what''s happening with constency actually what''s happening with constency
    actually what''s happening with constency

    training and that kind of deviates from training and that kind of deviates from
    training and that kind of deviates from

    a proper distribution matching objective a proper distribution matching objective
    a proper distribution matching objective

    um and this also partially explains why um and this also partially explains why
    um and this also partially explains why

    constency training is prone to collapse constency training is prone to collapse
    constency training is prone to collapse

    and the second uh the second work I want and the second uh the second work I want
    and the second uh the second work I want

    to mention is generative moment match to mention is generative moment match to
    mention is generative moment match

    network which came out 10 years ago. Um network which came out 10 years ago. Um
    network which came out 10 years ago. Um

    and G GMMN can also be seen as a special'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 35
  start_sec: 1924.63
  end_sec: 1973.6
  text: 'and G GMMN can also be seen as a special and G GMMN can also be seen as a
    special

    case of Imm. Uh case of Imm. Uh case of Imm. Uh

    you can easily see that when if you set you can easily see that when if you set
    you can easily see that when if you set

    TB uh to be identically equal to one and TB uh to be identically equal to one
    and TB uh to be identically equal to one and

    S and R to be identically equal to zero S and R to be identically equal to zero
    S and R to be identically equal to zero

    and you will exactly recover GMN''s and you will exactly recover GMN''s and you
    will exactly recover GMN''s

    training objective. training objective. training objective.

    But of course it''s it''s difficult to get But of course it''s it''s difficult
    to get But of course it''s it''s difficult to get

    it work uh to get it to work because it work uh to get it to work because it work
    uh to get it to work because

    well you have the same pro problem with well you have the same pro problem with
    well you have the same pro problem with

    MMD on in high emission uh where you MMD on in high emission uh where you MMD
    on in high emission uh where you

    have very little training signal. So the have very little training signal. So
    the have very little training signal. So the

    inductive learning uh component is is is inductive learning uh component is is
    is inductive learning uh component is is is

    a very necessary component a very necessary component a very necessary component

    and uh if you are following the and uh if you are following the and uh if you
    are following the

    literature closely uh you also may have literature closely uh you also may have
    literature closely uh you also may have

    seen this work uh from from Kimhood''s seen this work uh from from Kimhood''s
    seen this work uh from from Kimhood''s

    group uh called drifting model uh and group uh called drifting model uh and group
    uh called drifting model uh and

    essentially in this paper the drift essentially in this paper the drift'
  concept_slugs:
  - latent-diffusion
  - velocity-field
  - video-diffusion
- idx: 36
  start_sec: 1973.6
  end_sec: 2033.19
  text: 'essentially in this paper the drift

    field for their uh for their model is field for their uh for their model is field
    for their uh for their model is

    also parameterized via uh via MMD also parameterized via uh via MMD also parameterized
    via uh via MMD

    attraction plus MMD repulsion. So it''s attraction plus MMD repulsion. So it''s
    attraction plus MMD repulsion. So it''s

    it''s quite interesting that you know MMD it''s quite interesting that you know
    MMD it''s quite interesting that you know MMD

    has now uh is now getting some some has now uh is now getting some some has now
    uh is now getting some some

    attention from from a more modern attention from from a more modern attention
    from from a more modern

    perspective. Yeah. And and if you have perspective. Yeah. And and if you have
    perspective. Yeah. And and if you have

    not uh read this paper I highly not uh read this paper I highly not uh read this
    paper I highly

    recommend it. recommend it. recommend it.

    And And

    and before moving on uh I I also want to and before moving on uh I I also want
    to and before moving on uh I I also want to

    note several limitations of IMM. Um note several limitations of IMM. Um note several
    limitations of IMM. Um

    and one one is that uh MMD by design and one one is that uh MMD by design and
    one one is that uh MMD by design

    needs multiple samples to calculate the needs multiple samples to calculate the
    needs multiple samples to calculate the

    objective. So this adds some engineering objective. So this adds some engineering
    objective. So this adds some engineering

    burden at at large scale. Uh because say burden at at large scale. Uh because
    say burden at at large scale. Uh because say

    you are training a a large video model you are training a a large video model
    you are training a a large video model

    uh that that has larger of uh you know uh that that has larger of uh you know
    uh that that has larger of uh you know

    number of parameters the the batch size number of parameters the the batch size
    number of parameters the the batch size

    per GPU can can usually be as low as'
  concept_slugs:
  - latent-diffusion
  - velocity-field
  - video-diffusion
- idx: 37
  start_sec: 2033.19
  end_sec: 2085.03
  text: 'per GPU can can usually be as low as per GPU can can usually be as low as

    one. uh and in this case you know you one. uh and in this case you know you one.
    uh and in this case you know you

    need to gather from different GPUs to to need to gather from different GPUs to
    to need to gather from different GPUs to to

    instantiate the MMD matrix and and there instantiate the MMD matrix and and there
    instantiate the MMD matrix and and there

    are some pretty involved engineering are some pretty involved engineering are
    some pretty involved engineering

    tricks to to make it work. Um and I tricks to to make it work. Um and I tricks
    to to make it work. Um and I

    guess the sec the the second uh guess the sec the the second uh guess the sec
    the the second uh

    shortcoming is that uh R is is usually shortcoming is that uh R is is usually
    shortcoming is that uh R is is usually

    chosen to be very close to T and this chosen to be very close to T and this chosen
    to be very close to T and this

    naturally requires high precision for naturally requires high precision for naturally
    requires high precision for

    the network uh because the network the network uh because the network the network
    uh because the network

    itself needs to distinguish between itself needs to distinguish between itself
    needs to distinguish between

    close by R&T. uh but on large scale close by R&T. uh but on large scale close
    by R&T. uh but on large scale

    model you know people use lower model you know people use lower model you know
    people use lower

    precision training like BF-16 or even precision training like BF-16 or even precision
    training like BF-16 or even

    lower uh like people can use as low as lower uh like people can use as low as
    lower uh like people can use as low as

    like FP8 or or something like that. So like FP8 or or something like that. So
    like FP8 or or something like that. So

    so uh in that case if the model cannot so uh in that case if the model cannot
    so uh in that case if the model cannot

    distinguish between nearby R&T then it'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 38
  start_sec: 2085.03
  end_sec: 2136.32
  text: 'distinguish between nearby R&T then it distinguish between nearby R&T then
    it

    it''s generally uh harder to scale. it''s generally uh harder to scale. it''s
    generally uh harder to scale.

    So these are so these are the So these are so these are the So these are so these
    are the

    limitations that kind of motivated us to limitations that kind of motivated us
    to limitations that kind of motivated us to

    to approach the same problem from a to approach the same problem from a to approach
    the same problem from a

    different angle. Uh and and that kind of different angle. Uh and and that kind
    of different angle. Uh and and that kind of

    leads me uh to to our second work called leads me uh to to our second work called
    leads me uh to to our second work called

    terminal velocity matching. terminal velocity matching. terminal velocity matching.

    >> And this >> And this >> And this

    >> Alex before you >> Alex before you >> Alex before you

    any any questions from about any any questions from about any any questions from
    about

    >> I feel like there should be some Yeah. >> I feel like there should be some
    Yeah. >> I feel like there should be some Yeah.

    Go ahead. Can you elaborate more on like Go ahead. Can you elaborate more on like
    Go ahead. Can you elaborate more on like

    like what is like these kernels and like like what is like these kernels and like
    like what is like these kernels and like

    there there''s this there there''s this there there''s this

    >> Oh yeah yeah yeah >> Oh yeah yeah yeah >> Oh yeah yeah yeah

    >> what was like RK something can you >> what was like RK something can you >>
    what was like RK something can you

    elaborate on that I think it''s page 13 elaborate on that I think it''s page 13
    elaborate on that I think it''s page 13

    >> so so yeah so for for this right uh yeah >> so so yeah so for for this right
    uh yeah >> so so yeah so for for this right uh yeah

    so kernels is is a very uh standard um so kernels is is a very uh standard um'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 39
  start_sec: 2136.32
  end_sec: 2194.88
  text: 'so kernels is is a very uh standard um

    concept I guess in machine learning um concept I guess in machine learning um
    concept I guess in machine learning um

    it''s it it''s basically a a similarity it''s it it''s basically a a similarity
    it''s it it''s basically a a similarity

    function uh a symmetric similarity function uh a symmetric similarity function
    uh a symmetric similarity

    function uh of of two samples from a function uh of of two samples from a function
    uh of of two samples from a

    data space. So um data space. So um data space. So um

    uh how can I say this? So the kernels uh how can I say this? So the kernels uh
    how can I say this? So the kernels

    can be can be can be

    uh understood as a as an inner product uh understood as a as an inner product
    uh understood as a as an inner product

    in in in an augmented feature space like in in in an augmented feature space like
    in in in an augmented feature space like

    you know uh say say like your data is uh you know uh say say like your data is
    uh you know uh say say like your data is uh

    it is a number say your data is a number it is a number say your data is a number
    it is a number say your data is a number

    on a on a real line then you can augment on a on a real line then you can augment
    on a on a real line then you can augment

    it to to some high dimensional data it to to some high dimensional data it to
    to some high dimensional data

    space uh say say you can do some space uh say say you can do some space uh say
    say you can do some

    polomial on on on this real real data. polomial on on on this real real data.
    polomial on on on this real real data.

    Um and then you and you can augment it Um and then you and you can augment it
    Um and then you and you can augment it

    to to some um vector where each entry is to to some um vector where each entry
    is'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 40
  start_sec: 2194.88
  end_sec: 2248.48
  text: 'to to some um vector where each entry is

    like a uh a power of this real number like a uh a power of this real number like
    a uh a power of this real number

    and that is kind of a augmented feature and that is kind of a augmented feature
    and that is kind of a augmented feature

    space and the kernel is basically the space and the kernel is basically the space
    and the kernel is basically the

    inner product of these two feature inner product of these two feature inner product
    of these two feature

    space. Um yeah and it it''s a it''s a space. Um yeah and it it''s a it''s a space.
    Um yeah and it it''s a it''s a

    standard uh technique in in machine standard uh technique in in machine standard
    uh technique in in machine

    learning. Uh yeah. Um so you''ll see this learning. Uh yeah. Um so you''ll see
    this learning. Uh yeah. Um so you''ll see this

    in a lot of techniques like uh the in a lot of techniques like uh the in a lot
    of techniques like uh the

    classical classical classical

    uh things like uh SVM. I think you''ll uh things like uh SVM. I think you''ll
    uh things like uh SVM. I think you''ll

    you''ll see something like that. Yeah. So >> yeah. So the so Gen Z kids who probably
    >> yeah. So the so Gen Z kids who probably

    haven''t learned SVMs. So I I guess the haven''t learned SVMs. So I I guess the
    haven''t learned SVMs. So I I guess the

    closest thing that you guys probably closest thing that you guys probably closest
    thing that you guys probably

    heard of is like softmax attention, heard of is like softmax attention, heard
    of is like softmax attention,

    right? So you can imagine the soft right? So you can imagine the soft right? So
    you can imagine the soft

    tension is like kind of like a tension is like kind of like a tension is like
    kind of like a

    similarity matrix between the query and similarity matrix between the query and
    similarity matrix between the query and

    the and the and the keys right and this the and the and the keys right and this'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 41
  start_sec: 2248.48
  end_sec: 2295.44
  text: 'the and the and the keys right and this

    is sort of like basically we project the is sort of like basically we project
    the is sort of like basically we project the

    query and the keys to some feature space query and the keys to some feature space
    query and the keys to some feature space

    and then we calculate the inner product and then we calculate the inner product
    and then we calculate the inner product

    and this is actually how people also and this is actually how people also and
    this is actually how people also

    develop the linear attention. So this is develop the linear attention. So this
    is develop the linear attention. So this is

    kind of like you can sort of imagine kind of like you can sort of imagine kind
    of like you can sort of imagine

    kernels to be something like that. Yeah. kernels to be something like that. Yeah.
    kernels to be something like that. Yeah.

    >> Yeah. Yeah. Yeah. Yeah. Yeah. Uh the >> Yeah. Yeah. Yeah. Yeah. Yeah. Uh the
    >> Yeah. Yeah. Yeah. Yeah. Yeah. Uh the

    linear attention is a great application linear attention is a great application
    linear attention is a great application

    of kernels. Yes. Uh I highly recommend of kernels. Yes. Uh I highly recommend
    of kernels. Yes. Uh I highly recommend

    uh reading about it for sure. uh reading about it for sure. uh reading about it
    for sure.

    >> Any other questions? >> Okay. I have a question for the people. >> Okay. I
    have a question for the people.

    So we just talked about like consistency So we just talked about like consistency
    So we just talked about like consistency

    or you mentioned the consistency models or you mentioned the consistency models
    or you mentioned the consistency models

    but we also talked about like but we also talked about like but we also talked
    about like

    consistency trajectory models and flow consistency trajectory models and flow
    consistency trajectory models and flow

    maps in our previous lecture. Um so can maps in our previous lecture. Um so can
    maps in our previous lecture. Um so can

    you like maybe conceptually compare IM you like maybe conceptually compare IM
    you like maybe conceptually compare IM

    and also maybe like if you guys have and also maybe like if you guys have'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 42
  start_sec: 2295.44
  end_sec: 2360.23
  text: 'and also maybe like if you guys have

    tried like empirically like how do would tried like empirically like how do would
    tried like empirically like how do would

    you compare the three types of models? you compare the three types of models?
    you compare the three types of models?

    >> Yeah. So >> Yeah. So >> Yeah. So

    uh I can so consistency model it has two uh I can so consistency model it has
    two uh I can so consistency model it has two

    two things right it it it has the two things right it it it has the two things
    right it it it has the

    consistency dissolation and consistency consistency dissolation and consistency
    consistency dissolation and consistency

    training. So this is more uh related to training. So this is more uh related to
    training. So this is more uh related to

    consistency training. So in constency consistency training. So in constency consistency
    training. So in constency

    training you know it it has this uh let training you know it it has this uh let
    training you know it it has this uh let

    me me me

    so in in constency training it has um so in in constency training it has um so
    in in constency training it has um

    it has this uh it it uses the data it has this uh it it uses the data it has this
    uh it it uses the data

    sample right to estimate the uh the sample right to estimate the uh the sample
    right to estimate the uh the

    score right it I remember there''s this score right it I remember there''s this
    score right it I remember there''s this

    step where where it uses a data sample step where where it uses a data sample
    step where where it uses a data sample

    to estimate the score uh and that takes to estimate the score uh and that takes
    to estimate the score uh and that takes

    you from uh from the current input XT to you from uh from the current input XT
    to you from uh from the current input XT to

    some uh nearby uh to some nearby data some uh nearby uh to some nearby data some
    uh nearby uh to some nearby data

    point XR say. Um so what what we found'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 43
  start_sec: 2360.23
  end_sec: 2419.829
  text: 'point XR say. Um so what what we found point XR say. Um so what what we found

    is that uh because of the correlation is that uh because of the correlation is
    that uh because of the correlation

    through through through through the data through through through through the data
    through through through through the data

    sample uh you can cast it as as a sample uh you can cast it as as a sample uh
    you can cast it as as a

    distribution matching objective only if distribution matching objective only if
    distribution matching objective only if

    you use multiple particles. So uh say so you use multiple particles. So uh say
    so you use multiple particles. So uh say so

    now when you have the MMD objective um now when you have the MMD objective um
    now when you have the MMD objective um

    and you use just one particle then the and you use just one particle then the
    and you use just one particle then the

    MMD objective will just come down to the MMD objective will just come down to
    the MMD objective will just come down to the

    attraction term that''s just uh uh attraction term that''s just uh uh attraction
    term that''s just uh uh

    maximizing the kernel between between maximizing the kernel between between maximizing
    the kernel between between

    your training target and your current uh your training target and your current
    uh your training target and your current uh

    network. So for so in that case the network. So for so in that case the network.
    So for so in that case the

    consistent training the the kernel that consistent training the the kernel that
    consistent training the the kernel that

    they use for consistent training is they use for consistent training is they use
    for consistent training is

    negative L2 loss and uh yeah so it''s negative L2 loss and uh yeah so it''s negative
    L2 loss and uh yeah so it''s

    it''s quite a interesting connection um it''s quite a interesting connection um
    it''s quite a interesting connection um

    once you see it um once you see it um once you see it um

    but the fact that they use only one but the fact that they use only one but the
    fact that they use only one

    particle for training uh for for for'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 44
  start_sec: 2419.829
  end_sec: 2476.079
  text: 'particle for training uh for for for particle for training uh for for for

    training the model means that they are training the model means that they are
    training the model means that they are

    ignoring the uh they''re ignoring the ignoring the uh they''re ignoring the ignoring
    the uh they''re ignoring the

    repulsion term that''s natural from the repulsion term that''s natural from the
    repulsion term that''s natural from the

    MMD objective. MMD objective. MMD objective.

    Uh and that repulsion term turns out to Uh and that repulsion term turns out to
    Uh and that repulsion term turns out to

    be very uh very important to keep the be very uh very important to keep the be
    very uh very important to keep the

    model from not being collapsed. So yeah, model from not being collapsed. So yeah,
    model from not being collapsed. So yeah,

    so that''s sort of a intuition. so that''s sort of a intuition. so that''s sort
    of a intuition.

    Yeah. Yeah. Yeah.

    >> Yeah. Do you have you tried uh like any >> Yeah. Do you have you tried uh like
    any >> Yeah. Do you have you tried uh like any

    flow map method or um flow map method or um flow map method or um

    >> uh >> uh >> uh

    what do you mean by tried for what do you mean by tried for what do you mean by
    tried for

    >> like have you like empirically compared >> like have you like empirically compared
    >> like have you like empirically compared

    uh or or not or not to empir just like I uh or or not or not to empir just like
    I uh or or not or not to empir just like I

    I guess conceptually. I guess conceptually. I guess conceptually.

    >> Yeah. So the so by the time we wrote >> Yeah. So the so by the time we wrote
    >> Yeah. So the so by the time we wrote

    this paper the flow map concept has not this paper the flow map concept has not
    this paper the flow map concept has not

    really uh came out yet. So, really uh came out yet. So, really uh came out yet.
    So,

    >> uh, yeah, but but for the next work, I >> uh, yeah, but but for the next work,
    I'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 45
  start_sec: 2476.079
  end_sec: 2530.88
  text: '>> uh, yeah, but but for the next work, I

    guess it''ll be much closer to flow maps. guess it''ll be much closer to flow
    maps. guess it''ll be much closer to flow maps.

    >> All right. Cool. Cool. >> All right. Cool. Cool. >> All right. Cool. Cool.

    >> Cool. Yeah. >> Yeah. So, so for this um for for this >> Yeah. So, so for this
    um for for this

    paper um uh yeah it kind of go uh goes paper um uh yeah it kind of go uh goes
    paper um uh yeah it kind of go uh goes

    back to the concept of flows uh and back to the concept of flows uh and back to
    the concept of flows uh and

    tries to by bypass some of these tries to by bypass some of these tries to by
    bypass some of these

    disadvantages of IMM and and the paper disadvantages of IMM and and the paper
    disadvantages of IMM and and the paper

    is called terminal velocity matching. So, so here we give some intuition on So,
    so here we give some intuition on

    terminal velocity matching. Uh on the terminal velocity matching. Uh on the terminal
    velocity matching. Uh on the

    left we have our normal diffusion you left we have our normal diffusion you left
    we have our normal diffusion you

    know where where we define our data to know where where we define our data to
    know where where we define our data to

    have diffusion time zero and our and our have diffusion time zero and our and
    our have diffusion time zero and our and our

    uh prior to have diffusion time one and uh prior to have diffusion time one and
    uh prior to have diffusion time one and

    we follow this convention throughout we follow this convention throughout we follow
    this convention throughout

    throughout this talk um you know for for throughout this talk um you know for
    for throughout this talk um you know for for

    diffusion and flow matching the OD diffusion and flow matching the OD diffusion
    and flow matching the OD

    integral kind of traces out this this integral kind of traces out this this integral
    kind of traces out this this

    curved path in space which I''m sure all curved path in space which I''m sure
    all'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 46
  start_sec: 2530.88
  end_sec: 2591.76
  text: 'curved path in space which I''m sure all

    of you know um and on the right uh we of you know um and on the right uh we of
    you know um and on the right uh we

    have uh have uh have uh

    a a model train trend via TVM. Uh and as a a model train trend via TVM. Uh and
    as a a model train trend via TVM. Uh and as

    mentioned before the two time the two mentioned before the two time the two mentioned
    before the two time the two

    time step DDIM sampler can now directly time step DDIM sampler can now directly
    time step DDIM sampler can now directly

    represent the displacement represent the displacement represent the displacement

    of the OD integral uh instead of the of the OD integral uh instead of the of the
    OD integral uh instead of the

    velocity field. So this results in a velocity field. So this results in a velocity
    field. So this results in a

    straight path connecting any two point straight path connecting any two point
    straight path connecting any two point

    on the OD. on the OD. on the OD.

    And this path uh is learned about uh And this path uh is learned about uh And
    this path uh is learned about uh

    simply matching this terminal velocity simply matching this terminal velocity
    simply matching this terminal velocity

    vector vector vector

    uh uh for for all points along this OD uh uh for for all points along this OD
    uh uh for for all points along this OD

    trajectory. trajectory. trajectory.

    And this is kind of a rough intuition uh And this is kind of a rough intuition
    uh And this is kind of a rough intuition uh

    but but let''s now look at an but but let''s now look at an but but let''s now
    look at an

    illustration of the these previous illustration of the these previous illustration
    of the these previous

    figures. So for division and flow matching um we So for division and flow matching
    um we

    visualize here the OD trajectory um visualize here the OD trajectory um visualize
    here the OD trajectory um

    connecting a data point uh x0 and a connecting a data point uh x0 and a connecting
    a data point uh x0 and a

    prior x1. prior x1.'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 47
  start_sec: 2591.76
  end_sec: 2655.68
  text: 'prior x1.

    So the tangent along this OD trajectory So the tangent along this OD trajectory
    So the tangent along this OD trajectory

    is the marginal velocity is the marginal velocity is the marginal velocity

    and this marginal velocity exists and in and this marginal velocity exists and
    in and this marginal velocity exists and in

    in diffusion flow matching we use a in diffusion flow matching we use a in diffusion
    flow matching we use a

    neuronet network to approximate it. uh neuronet network to approximate it. uh
    neuronet network to approximate it. uh

    and we note the map from XT to XS uh as and we note the map from XT to XS uh as
    and we note the map from XT to XS uh as

    the integral following as the integral the integral following as the integral
    the integral following as the integral

    following this uh tangent uh tangent following this uh tangent uh tangent following
    this uh tangent uh tangent

    velocity vector velocity vector velocity vector

    and for simplicity you know we we call and for simplicity you know we we call
    and for simplicity you know we we call

    we call this net net displacement uh as we call this net net displacement uh as
    we call this net net displacement uh as

    F here F here F here

    uh and now let''s look at TVM uh for for uh and now let''s look at TVM uh for
    for uh and now let''s look at TVM uh for for

    the same trajectory and ground truth the same trajectory and ground truth the
    same trajectory and ground truth

    displacement uh we instead use a neuronet network you uh we instead use a neuronet
    network you

    know to directly parameterize the know to directly parameterize the know to directly
    parameterize the

    displacement from from XT to XS uh in displacement from from XT to XS uh in displacement
    from from XT to XS uh in

    one neuronet network call one neuronet network call one neuronet network call

    and this results in a straight line and this results in a straight line and this
    results in a straight line

    and um and we call this you know onestep and um and we call this you know onestep
    and um and we call this you know onestep

    displacement f theta displacement f theta'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 48
  start_sec: 2655.68
  end_sec: 2711.75
  text: 'displacement f theta

    uh which we can define um you know as uh uh which we can define um you know as
    uh uh which we can define um you know as uh

    s minus t * capital f where where s minus t * capital f where where s minus t
    * capital f where where

    capital F is our actual neural network capital F is our actual neural network
    capital F is our actual neural network

    and here we we use this factor of S and here we we use this factor of S and here
    we we use this factor of S

    minus T by simply following the DDIM minus T by simply following the DDIM minus
    T by simply following the DDIM

    formula because it nicely satisfies the formula because it nicely satisfies the
    formula because it nicely satisfies the

    boundary condition uh of integral being boundary condition uh of integral being
    boundary condition uh of integral being

    zero. Uh and and here uh our our zero. Uh and and here uh our our zero. Uh and
    and here uh our our

    straight our straight path now is simply straight our straight path now is simply
    straight our straight path now is simply

    a onestep ddim. a onestep ddim. a onestep ddim.

    So now in the ideal case um what we So now in the ideal case um what we So now
    in the ideal case um what we

    actually want to learn right is is this actually want to learn right is is this
    actually want to learn right is is this

    displacement map from time t to time displacement map from time t to time displacement
    map from time t to time

    zero right because we want our model to zero right because we want our model to
    zero right because we want our model to

    uh in one step to to be able to produce uh in one step to to be able to produce
    uh in one step to to be able to produce

    a clean sample given given a noisy a clean sample given given a noisy a clean
    sample given given a noisy

    sample right so we want to learn this sample right so we want to learn this sample
    right so we want to learn this

    map that directly takes xt to x0'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 49
  start_sec: 2711.75
  end_sec: 2760.72
  text: 'map that directly takes xt to x0 map that directly takes xt to x0

    so naively uh what we want to learn oh so naively uh what we want to learn oh
    so naively uh what we want to learn oh

    how How we can learn it is to uh use how How we can learn it is to uh use how
    How we can learn it is to uh use

    this the simplest L2 loss uh between our this the simplest L2 loss uh between
    our this the simplest L2 loss uh between our

    our parameters map right f F data that our parameters map right f F data that
    our parameters map right f F data that

    take from t two time zero and match it take from t two time zero and match it
    take from t two time zero and match it

    against the ground truth OD so this is against the ground truth OD so this is
    against the ground truth OD so this is

    the naive approach uh and and what we the naive approach uh and and what we the
    naive approach uh and and what we

    ultimately want to learn ultimately want to learn ultimately want to learn

    um and if this is minimized you know for um and if this is minimized you know
    for um and if this is minimized you know for

    all trajectories then our model has all trajectories then our model has all trajectories
    then our model has

    learned the onestep learned the onestep learned the onestep

    But obviously we don''t want to perform But obviously we don''t want to perform
    But obviously we don''t want to perform

    integration for each step we train. So integration for each step we train. So
    integration for each step we train. So

    we need to somehow bypass this explicit we need to somehow bypass this explicit
    we need to somehow bypass this explicit

    integration step. So to do that um what integration step. So to do that um what
    integration step. So to do that um what

    what we actually want to look uh what we what we actually want to look uh what
    we what we actually want to look uh what we

    actually want to look at is this actually want to look at is this'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 50
  start_sec: 2760.72
  end_sec: 2823.599
  text: 'actually want to look at is this

    quantity um which which characterizes quantity um which which characterizes quantity
    um which which characterizes

    the the terminal velocity uh the the the the terminal velocity uh the the the
    the terminal velocity uh the the

    velocity at the terminal point of your velocity at the terminal point of your
    velocity at the terminal point of your

    parameterized map. parameterized map. parameterized map.

    So in fact for uh for each displacement So in fact for uh for each displacement
    So in fact for uh for each displacement

    map you construct there exists a a map you construct there exists a a map you
    construct there exists a a

    terminal velocity for for this uh for terminal velocity for for this uh for terminal
    velocity for for this uh for

    this displacement map. So so now I want to also bring to your So so now I want
    to also bring to your

    attention a particular uh property right attention a particular uh property right
    attention a particular uh property right

    of of the ground truth displacement. of of the ground truth displacement. of of
    the ground truth displacement.

    Um Um

    uh so for so so this is a uh sufficient uh so for so so this is a uh sufficient
    uh so for so so this is a uh sufficient

    condition um which we call the ter condition um which we call the ter condition
    um which we call the ter

    terminal velocity condition and so this terminal velocity condition and so this
    terminal velocity condition and so this

    is a sufficient condition for you to is a sufficient condition for you to is a
    sufficient condition for you to

    learn the ground truth displacement map learn the ground truth displacement map
    learn the ground truth displacement map

    and what it says is that basically the and what it says is that basically the
    and what it says is that basically the

    the the terminal uh velocity at uh for the the terminal uh velocity at uh for
    the the terminal uh velocity at uh for

    for this displacement map needs to match for this displacement map needs to match
    for this displacement map needs to match

    if it happens to match the marginal if it happens to match the marginal'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 51
  start_sec: 2823.599
  end_sec: 2887.68
  text: 'if it happens to match the marginal

    velocity at this point then you have velocity at this point then you have velocity
    at this point then you have

    automatically learned this this automatically learned this this automatically
    learned this this

    displacement map. displacement map. displacement map.

    So what it says is that if your model So what it says is that if your model So
    what it says is that if your model

    parameterized map uh the its terminal parameterized map uh the its terminal parameterized
    map uh the its terminal

    velocity if it happens to match the the velocity if it happens to match the the
    velocity if it happens to match the the

    ground truth uh velocity at xs then you ground truth uh velocity at xs then you
    ground truth uh velocity at xs then you

    have learned this onestep map. So, so here we note uh the the actual uh So, so
    here we note uh the the actual uh

    displacement error uh that we want to displacement error uh that we want to displacement
    error uh that we want to

    ultimately optimize and we essentially ultimately optimize and we essentially
    ultimately optimize and we essentially

    bypass this explicit integration step by bypass this explicit integration step
    by bypass this explicit integration step by

    matching the derivative instead. And you matching the derivative instead. And
    you matching the derivative instead. And you

    can also show that this uh this terminal can also show that this uh this terminal
    can also show that this uh this terminal

    velocity error upper bounds the velocity error upper bounds the velocity error
    upper bounds the

    displacement error. And trivially you displacement error. And trivially you displacement
    error. And trivially you

    know the the bound becomes tight if if know the the bound becomes tight if if
    know the the bound becomes tight if if

    each velocity matching loss inside this each velocity matching loss inside this
    each velocity matching loss inside this

    integral is zero which is the case when integral is zero which is the case when
    integral is zero which is the case when

    you perfectly match the terminal you perfectly match the terminal you perfectly
    match the terminal

    velocity velocity velocity

    and this is best shown uh in in this and this is best shown uh in in this'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 52
  start_sec: 2887.68
  end_sec: 2946.319
  text: 'and this is best shown uh in in this

    figure uh in the previous slides. Um so figure uh in the previous slides. Um so
    figure uh in the previous slides. Um so

    this is the case when when uh the bound this is the case when when uh the bound
    this is the case when when uh the bound

    is tight where is tight where is tight where

    where uh you know the the terminal where uh you know the the terminal where uh
    you know the the terminal

    velocity vector uh perfectly matches the velocity vector uh perfectly matches
    the velocity vector uh perfectly matches the

    tangent along this OD trajectory. So tangent along this OD trajectory. So tangent
    along this OD trajectory. So

    this is so this is when you perfectly this is so this is when you perfectly this
    is so this is when you perfectly

    learn this map and you can imagine that learn this map and you can imagine that
    learn this map and you can imagine that

    uh this this uh velocity vector kind of uh this this uh velocity vector kind of
    uh this this uh velocity vector kind of

    guides the onestep map all the way from guides the onestep map all the way from
    guides the onestep map all the way from

    the initial point to the final point uh the initial point to the final point uh
    the initial point to the final point uh

    to generate a sample. So uh h however if you notice uh we have So uh h however
    if you notice uh we have

    assumed that we need to have access to assumed that we need to have access to
    assumed that we need to have access to

    this ground truth u and ground truth f this ground truth u and ground truth f
    this ground truth u and ground truth f

    right so we don''t know that uh during right so we don''t know that uh during
    right so we don''t know that uh during

    pre-training time right so so this is a pre-training time right so so this is
    a pre-training time right so so this is a

    problem so this these quantities are problem so this these quantities are problem
    so this these quantities are

    these quantities exist but we don''t know these quantities exist but we don''t
    know'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 53
  start_sec: 2946.319
  end_sec: 3002.15
  text: 'these quantities exist but we don''t know

    that during pre pre-training time so how that during pre pre-training time so
    how that during pre pre-training time so how

    do we so how do we kind of have access do we so how do we kind of have access
    do we so how do we kind of have access

    to these. So what do you do in this to these. So what do you do in this to these.
    So what do you do in this

    case? case? case?

    Um it turns out we can just use our own Um it turns out we can just use our own
    Um it turns out we can just use our own

    network as as proxy for for the ground network as as proxy for for the ground
    network as as proxy for for the ground

    truth. truth. truth.

    But so so yeah, so here the this is the But so so yeah, so here the this is the
    But so so yeah, so here the this is the

    actual quantity that we wanted to have actual quantity that we wanted to have
    actual quantity that we wanted to have

    access to. But now we can just use our access to. But now we can just use our
    access to. But now we can just use our

    own network to kind of approximate these own network to kind of approximate these
    own network to kind of approximate these

    these two quantities. these two quantities. these two quantities.

    But you know uh this is a terrible But you know uh this is a terrible But you
    know uh this is a terrible

    approximation at the start of the approximation at the start of the approximation
    at the start of the

    training. So how do you uh so how do you training. So how do you uh so how do
    you training. So how do you uh so how do you

    make the training make sense right? Um make the training make sense right? Um
    make the training make sense right? Um

    so we additionally ensure that uh the so we additionally ensure that uh the so
    we additionally ensure that uh the

    the velocity parameterized by your by the velocity parameterized by your by the
    velocity parameterized by your by

    your own network u approximates the the'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 54
  start_sec: 3002.15
  end_sec: 3056.549
  text: 'your own network u approximates the the your own network u approximates the
    the

    ground truth velocity at at every single ground truth velocity at at every single
    ground truth velocity at at every single

    point. And this can be done by a simple point. And this can be done by a simple
    point. And this can be done by a simple

    flow matching loss. flow matching loss. flow matching loss.

    So our final objective now becomes this. So our final objective now becomes this.
    So our final objective now becomes this.

    So we we optimize our terminal velocity So we we optimize our terminal velocity
    So we we optimize our terminal velocity

    error uh in conjunction with a flow error uh in conjunction with a flow error
    uh in conjunction with a flow

    matching loss. And I won''t go into too matching loss. And I won''t go into too
    matching loss. And I won''t go into too

    much detail on this but the f theta here much detail on this but the f theta here
    much detail on this but the f theta here

    and u theta here can be parameterized by and u theta here can be parameterized
    by and u theta here can be parameterized by

    the same network. And up to this point uh some may think And up to this point
    uh some may think

    okay the the combination of the two okay the the combination of the two okay the
    the combination of the two

    losses seem like a hacky choice to get losses seem like a hacky choice to get
    losses seem like a hacky choice to get

    the algorithm to work but it turns out the algorithm to work but it turns out
    the algorithm to work but it turns out

    that the TVM loss that we have that we that the TVM loss that we have that we
    that the TVM loss that we have that we

    have proposed um uh is is very closely have proposed um uh is is very closely
    have proposed um uh is is very closely

    related to distribution matching. So related to distribution matching. So related
    to distribution matching. So

    specifically uh we show in our paper specifically uh we show in our paper specifically
    uh we show in our paper

    that uh TVM loss upper bounds the two'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 55
  start_sec: 3056.549
  end_sec: 3114.8
  text: 'that uh TVM loss upper bounds the two that uh TVM loss upper bounds the two

    wound distance up to some constant and wound distance up to some constant and
    wound distance up to some constant and

    this is also why we did not introduce this is also why we did not introduce this
    is also why we did not introduce

    any balancing factors uh between the two any balancing factors uh between the
    two any balancing factors uh between the two

    terms uh because it might deviate from terms uh because it might deviate from
    terms uh because it might deviate from

    this distribution matching this distribution matching this distribution matching

    interpretation. interpretation. interpretation.

    Um although in practice you know you can Um although in practice you know you
    can Um although in practice you know you can

    definitely try balancing those two two definitely try balancing those two two
    definitely try balancing those two two

    terms with with some factor but we did terms with with some factor but we did
    terms with with some factor but we did

    not try it because you know uh without not try it because you know uh without
    not try it because you know uh without

    without any factor it already works without any factor it already works without
    any factor it already works

    pretty well. So this kind of also pretty well. So this kind of also pretty well.
    So this kind of also

    justifies the addition of the two two justifies the addition of the two two justifies
    the addition of the two two

    loss terms from a more theoretical loss terms from a more theoretical loss terms
    from a more theoretical

    perspective. perspective. perspective.

    And there there''s another important And there there''s another important And
    there there''s another important

    implication from this result which is implication from this result which is implication
    from this result which is

    that the bound here actually depends on that the bound here actually depends on
    that the bound here actually depends on

    the lipousness of your neur neuronet the lipousness of your neur neuronet the
    lipousness of your neur neuronet

    network. uh but mo but importantly network. uh but mo but importantly network.
    uh but mo but importantly

    modern diffusion transformers are modern diffusion transformers are modern diffusion
    transformers are

    actually not lies continuous because of actually not lies continuous because of'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 56
  start_sec: 3114.8
  end_sec: 3171.51
  text: 'actually not lies continuous because of

    the dot product self attention and layer the dot product self attention and layer
    the dot product self attention and layer

    norms and there''s actually a lot of norms and there''s actually a lot of norms
    and there''s actually a lot of

    literature that studies that STPA and literature that studies that STPA and literature
    that studies that STPA and

    layer norms are not lies continuous so layer norms are not lies continuous so
    layer norms are not lies continuous so

    so so we need some ways to constrain the so so we need some ways to constrain
    the so so we need some ways to constrain the

    lipousness of your network but of course lipousness of your network but of course
    lipousness of your network but of course

    uh it''s it''s kind of difficult to hard uh it''s it''s kind of difficult to hard
    uh it''s it''s kind of difficult to hard

    constrain the liciousness um in general. constrain the liciousness um in general.
    constrain the liciousness um in general.

    So we want to introduce some simple So we want to introduce some simple So we
    want to introduce some simple

    changes to the naive diffusion changes to the naive diffusion changes to the naive
    diffusion

    transformers to perform what I call a transformers to perform what I call a transformers
    to perform what I call a

    semi semi lipous control right so these semi semi lipous control right so these
    semi semi lipous control right so these

    changes are very simple and non-invasive changes are very simple and non-invasive
    changes are very simple and non-invasive

    so these are broad broadly very so these are broad broadly very so these are broad
    broadly very

    applicable applicable applicable

    so some examples uh well the most so some examples uh well the most so some examples
    uh well the most

    important changes that we proposed is important changes that we proposed is important
    changes that we proposed is

    changing layer norms to RMS norm and we changing layer norms to RMS norm and we
    changing layer norms to RMS norm and we

    use RMS norm as QK norm and we and and use RMS norm as QK norm and we and and
    use RMS norm as QK norm and we and and

    we you know add add RMS norm as uh'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 57
  start_sec: 3171.51
  end_sec: 3233.2
  text: 'we you know add add RMS norm as uh we you know add add RMS norm as uh

    without any parameters uh to the time without any parameters uh to the time without
    any parameters uh to the time

    step modulation before we input into uh step modulation before we input into uh
    step modulation before we input into uh

    add layers. So you can show that with add layers. So you can show that with add
    layers. So you can show that with

    these simple changes each of the modules these simple changes each of the modules
    these simple changes each of the modules

    now become lip bounded and and they now become lip bounded and and they now become
    lip bounded and and they

    greatly help uh training stability. greatly help uh training stability. greatly
    help uh training stability.

    And this lip related insight uh also And this lip related insight uh also And
    this lip related insight uh also

    kind of reveals the flaws in current kind of reveals the flaws in current kind
    of reveals the flaws in current

    diffusion transformer design u diffusion transformer design u diffusion transformer
    design u

    especially for training onestep models. Okay. Um Okay. Um

    and yeah so so now we have seen this uh and yeah so so now we have seen this uh
    and yeah so so now we have seen this uh

    DFDS term a lot but how do we actually DFDS term a lot but how do we actually
    DFDS term a lot but how do we actually

    calculate it right um how do you calculate it right um how do you calculate it
    right um how do you

    actually so let''s first recall um that actually so let''s first recall um that
    actually so let''s first recall um that

    we defined our f theta to be sus t * big we defined our f theta to be sus t *
    big we defined our f theta to be sus t * big

    capital f capital f capital f

    and where where capital f is our actual and where where capital f is our actual
    and where where capital f is our actual

    neur neural network neur neural network neur neural network

    and you can do some quick mental math uh and you can do some quick mental math
    uh'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 58
  start_sec: 3233.2
  end_sec: 3289.43
  text: 'and you can do some quick mental math uh

    to just take derivative with respect to to just take derivative with respect to
    to just take derivative with respect to

    s on both sides, right? And s on both sides, right? And s on both sides, right?
    And

    after some chain rule, what what you after some chain rule, what what you after
    some chain rule, what what you

    will get is actually this term, right? will get is actually this term, right?
    will get is actually this term, right?

    So is actually just a addition of a So is actually just a addition of a So is
    actually just a addition of a

    model for call plus model for call plus model for call plus

    you know uh a partial derivative term you know uh a partial derivative term you
    know uh a partial derivative term

    with with respect to s. with with respect to s. with with respect to s.

    And um I want to bring to your attention And um I want to bring to your attention
    And um I want to bring to your attention

    the second term here uh here for for the second term here uh here for for the
    second term here uh here for for

    this term for this partial derivative this term for this partial derivative this
    term for this partial derivative

    with respect to your model input s. This with respect to your model input s. This
    with respect to your model input s. This

    uh can can be done by u jacobian vector uh can can be done by u jacobian vector
    uh can can be done by u jacobian vector

    product or JVP. product or JVP. product or JVP.

    And for those of you that are familiar And for those of you that are familiar
    And for those of you that are familiar

    with meanflow uh it it also uses JVP for with meanflow uh it it also uses JVP
    for with meanflow uh it it also uses JVP for

    it training. But here I want to note it training. But here I want to note it training.
    But here I want to note

    some differences. uh uh so here we don''t some differences. uh uh so here we don''t
    some differences. uh uh so here we don''t

    have any stop gradient um which means'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 59
  start_sec: 3289.43
  end_sec: 3339.359
  text: 'have any stop gradient um which means have any stop gradient um which means

    that we ideally want to back propagate that we ideally want to back propagate
    that we ideally want to back propagate

    through this this JVP term but of course through this this JVP term but of course
    through this this JVP term but of course

    uh in practice you you can also try like uh in practice you you can also try like
    uh in practice you you can also try like

    adding a stop grat specifically for this adding a stop grat specifically for this
    adding a stop grat specifically for this

    term just like meanflow uh but this will term just like meanflow uh but this will
    term just like meanflow uh but this will

    just give you a biased gradient when you just give you a biased gradient when
    you just give you a biased gradient when you

    are trying to optimize the uh the are trying to optimize the uh the are trying
    to optimize the uh the

    overall objective overall objective overall objective

    and the the second difference. Uh oh and the the second difference. Uh oh and
    the the second difference. Uh oh

    yeah. So, so to to to propagate through yeah. So, so to to to propagate through
    yeah. So, so to to to propagate through

    the GVP term, we will need to implement the GVP term, we will need to implement
    the GVP term, we will need to implement

    PyTorch kernels uh to support the PyTorch kernels uh to support the PyTorch kernels
    uh to support the

    backward pass uh through the through the backward pass uh through the through
    the backward pass uh through the through the

    GVP. GVP. GVP.

    And the second difference is that the And the second difference is that the And
    the second difference is that the

    JVP is actually only taken with respect JVP is actually only taken with respect
    JVP is actually only taken with respect

    to time S. Um so it is invariant to XC to time S. Um so it is invariant to XC
    to time S. Um so it is invariant to XC

    and T. and T. and T.

    So this is actually exactly opposite of So this is actually exactly opposite of'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 60
  start_sec: 3339.359
  end_sec: 3398.0
  text: 'So this is actually exactly opposite of

    meanflow which takes partial on both xt meanflow which takes partial on both xt
    meanflow which takes partial on both xt

    and t. and t. and t.

    Yeah. Uh so I will I will say say this Yeah. Uh so I will I will say say this
    Yeah. Uh so I will I will say say this

    much about this method and if you if you much about this method and if you if
    you much about this method and if you if you

    forget everything about the math just forget everything about the math just forget
    everything about the math just

    just just remember this figure where uh just just remember this figure where uh
    just just remember this figure where uh

    where where the terminal velocity when where where the terminal velocity when
    where where the terminal velocity when

    when it perfectly matches you know the when it perfectly matches you know the
    when it perfectly matches you know the

    branch velocity you will be able to branch velocity you will be able to branch
    velocity you will be able to

    learn this one step map. Okay. Um

    and for for some experimental results we and for for some experimental results
    we and for for some experimental results we

    empirically find that you know compared empirically find that you know compared
    empirically find that you know compared

    to mean inflow uh our objective gives to mean inflow uh our objective gives to
    mean inflow uh our objective gives

    very stable gradient profile and as you very stable gradient profile and as you
    very stable gradient profile and as you

    can see here in the figure uh especially can see here in the figure uh especially
    can see here in the figure uh especially

    when when uh when there''s random CFG when when uh when there''s random CFG when
    when uh when there''s random CFG

    during training the gradient norm of during training the gradient norm of during
    training the gradient norm of

    mean flow can can fluctuate a lot. Um mean flow can can fluctuate a lot. Um mean
    flow can can fluctuate a lot. Um

    but for TVM uh the gradient profile is but for TVM uh the gradient profile is
    but for TVM uh the gradient profile is

    very stable. very stable.'
  concept_slugs:
  - classifier-free-guidance
  - latent-diffusion
  - video-diffusion
- idx: 61
  start_sec: 3398.0
  end_sec: 3452.95
  text: 'very stable.

    And if we track also the norm of the And if we track also the norm of the And
    if we track also the norm of the

    marginal velocity uh for both mean flow marginal velocity uh for both mean flow
    marginal velocity uh for both mean flow

    and TVM under this under the random CFG and TVM under this under the random CFG
    and TVM under this under the random CFG

    setting we also see that uh TVM has very setting we also see that uh TVM has very
    setting we also see that uh TVM has very

    smooth gradient profile. Oh sorry very smooth gradient profile. Oh sorry very
    smooth gradient profile. Oh sorry very

    smooth uh norm uh for for for the smooth uh norm uh for for for the smooth uh
    norm uh for for for the

    marginal velocity. marginal velocity. marginal velocity.

    And I think part of the reason uh for me And I think part of the reason uh for
    me And I think part of the reason uh for me

    for mfo to to be unstable for mfo to to be unstable for mfo to to be unstable

    is that it needs to propagate UT uh is that it needs to propagate UT uh is that
    it needs to propagate UT uh

    through through this term uh through the through through this term uh through
    the through through this term uh through the

    XT term. So remember that uh meanflow XT term. So remember that uh meanflow XT
    term. So remember that uh meanflow

    calculates JVP uh with respect to XT and calculates JVP uh with respect to XT
    and calculates JVP uh with respect to XT and

    T. So so so it needs a tangent vector UT T. So so so it needs a tangent vector
    UT T. So so so it needs a tangent vector UT

    to be to be propagated through XT. to be to be propagated through XT. to be to
    be propagated through XT.

    And in practice uh this tangent vector And in practice uh this tangent vector
    And in practice uh this tangent vector

    for mean flow is a combination of of for mean flow is a combination of of for
    mean flow is a combination of of

    network predicted velocity and uh and um'
  concept_slugs:
  - classifier-free-guidance
  - latent-diffusion
  - video-diffusion
- idx: 62
  start_sec: 3452.95
  end_sec: 3514.319
  text: 'network predicted velocity and uh and um network predicted velocity and uh
    and um

    conditional velocity and there are conditional velocity and there are conditional
    velocity and there are

    additional variance uh that''s being additional variance uh that''s being additional
    variance uh that''s being

    introduced into the tangent calculation introduced into the tangent calculation
    introduced into the tangent calculation

    um which can stabil destabilize uh the um which can stabil destabilize uh the
    um which can stabil destabilize uh the

    JVP and because JVP in itself is is JVP and because JVP in itself is is JVP and
    because JVP in itself is is

    actually not very stable um for now uh actually not very stable um for now uh
    actually not very stable um for now uh

    for all these packages so so propagating for all these packages so so propagating
    for all these packages so so propagating

    uh some some uh some noise vectors uh is uh some some uh some noise vectors uh
    is uh some some uh some noise vectors uh is

    going to cause uh some stability going to cause uh some stability going to cause
    uh some stability

    problem. problem. problem.

    But for TVM uh since we don''t need But for TVM uh since we don''t need But for
    TVM uh since we don''t need

    partial partial with with respect to XT partial partial with with respect to XT
    partial partial with with respect to XT

    and T and we only need partial with and T and we only need partial with and T
    and we only need partial with

    respect to S. So the tangent vector uh respect to S. So the tangent vector uh
    respect to S. So the tangent vector uh

    for the GVP is is just constant 001. Um for the GVP is is just constant 001. Um
    for the GVP is is just constant 001. Um

    and that stays the same stays the same and that stays the same stays the same
    and that stays the same stays the same

    for all sampled XT. um and that''s for all sampled XT. um and that''s for all
    sampled XT. um and that''s

    because it''s invariant to them. So the because it''s invariant to them. So the
    because it''s invariant to them. So the

    JVP term can be stably optimized >> and yeah um experimentally we achieve'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 63
  start_sec: 3514.319
  end_sec: 3567.43
  text: '>> and yeah um experimentally we achieve

    still there one step result on imaget still there one step result on imaget still
    there one step result on imaget

    and it can also surpass uh dn and xit and it can also surpass uh dn and xit and
    it can also surpass uh dn and xit

    with four step um and we can get similar with four step um and we can get similar
    with four step um and we can get similar

    similar results uh compared to baseline similar results uh compared to baseline
    similar results uh compared to baseline

    for imaging at 512 and 512. Uh here are for imaging at 512 and 512. Uh here are
    for imaging at 512 and 512. Uh here are

    some samples from both the 256 some samples from both the 256 some samples from
    both the 256

    resolution and 512 resolution and these resolution and 512 resolution and these
    resolution and 512 resolution and these

    are produced with just uh one step are produced with just uh one step are produced
    with just uh one step

    and and and

    but you know since since nowadays every but you know since since nowadays every
    but you know since since nowadays every

    every method you know can perform well every method you know can perform well
    every method you know can perform well

    on imageet so so we had this follow-up on imageet so so we had this follow-up
    on imageet so so we had this follow-up

    effort to try to scale it to 10 10 effort to try to scale it to 10 10 effort to
    try to scale it to 10 10

    billion plus parameter scale uh for text billion plus parameter scale uh for text
    billion plus parameter scale uh for text

    to image and this is what I and this is to image and this is what I and this is
    to image and this is what I and this is

    kind of what I wanted to show for for kind of what I wanted to show for for kind
    of what I wanted to show for for

    this work is that TVM works well at this work is that TVM works well at this work
    is that TVM works well at

    scale and this model is is trained with'
  concept_slugs:
  - image-generation
  - latent-diffusion
  - video-diffusion
- idx: 64
  start_sec: 3567.43
  end_sec: 3616.309
  text: 'scale and this model is is trained with scale and this model is is trained
    with

    pure TVM loss uh closely following what pure TVM loss uh closely following what
    pure TVM loss uh closely following what

    our paper has has has uh proposed. So our paper has has has uh proposed. So our
    paper has has has uh proposed. So

    the quality does transfer at scale and the quality does transfer at scale and
    the quality does transfer at scale and

    you can notice that it has some pretty you can notice that it has some pretty
    you can notice that it has some pretty

    good um tech text rendering and text good um tech text rendering and text good
    um tech text rendering and text

    rendering as well. Um, and all of these rendering as well. Um, and all of these
    rendering as well. Um, and all of these

    samples are generated by Forstep TVM. samples are generated by Forstep TVM. samples
    are generated by Forstep TVM.

    And if you''re interested, you can also And if you''re interested, you can also
    And if you''re interested, you can also

    go to our blog here. Uh, and there are go to our blog here. Uh, and there are
    go to our blog here. Uh, and there are

    some more samples that that that you can some more samples that that that you
    can some more samples that that that you can

    look at. And there''s also a fung look at. And there''s also a fung look at. And
    there''s also a fung

    guessing game that you can play with. guessing game that you can play with. guessing
    game that you can play with.

    So, um, lastly, I want to note some So, um, lastly, I want to note some So, um,
    lastly, I want to note some

    challenges at scale. So, first is that challenges at scale. So, first is that
    challenges at scale. So, first is that

    the JVP, uh, in PyTorch does not work the JVP, uh, in PyTorch does not work the
    JVP, uh, in PyTorch does not work

    super well with FSTP. the uh so so for super well with FSTP. the uh so so for
    super well with FSTP. the uh so so for

    for uh FSTP if you naively call JVP on'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 65
  start_sec: 3616.309
  end_sec: 3667.99
  text: 'for uh FSTP if you naively call JVP on for uh FSTP if you naively call JVP
    on

    the entire FSTP sharded model the entire FSTP sharded model the entire FSTP sharded
    model

    uh then FSTP will usually error out uh then FSTP will usually error out uh then
    FSTP will usually error out

    because JVP doesn''t have a good good because JVP doesn''t have a good good because
    JVP doesn''t have a good good

    support of it and it can''t find support of it and it can''t find support of it
    and it can''t find

    parameters which exist on other devices. parameters which exist on other devices.
    parameters which exist on other devices.

    Uh so our solution for for this was to Uh so our solution for for this was to
    Uh so our solution for for this was to

    wrap the JVP inside each layer of the wrap the JVP inside each layer of the wrap
    the JVP inside each layer of the

    model um before before it''s being model um before before it''s being model um
    before before it''s being

    sharded. So what so what happened was uh sharded. So what so what happened was
    uh sharded. So what so what happened was uh

    for each uh layer inside the the big for each uh layer inside the the big for
    each uh layer inside the the big

    model we have a specific uh we have a model we have a specific uh we have a model
    we have a specific uh we have a

    specific JVP forward call um so that specific JVP forward call um so that specific
    JVP forward call um so that

    when when the model is being sharded the when when the model is being sharded
    the when when the model is being sharded the

    JVP operation can can be safely done uh JVP operation can can be safely done uh
    JVP operation can can be safely done uh

    on on the layers that exist on the same on on the layers that exist on the same
    on on the layers that exist on the same

    device. device. device.

    Oh yeah. Uh yeah. So this is the the Oh yeah. Uh yeah. So this is the the Oh yeah.
    Uh yeah. So this is the the

    first challenge with uh FSTP with JVP'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 66
  start_sec: 3667.99
  end_sec: 3718.0
  text: 'first challenge with uh FSTP with JVP first challenge with uh FSTP with JVP

    and the second challenge was is uh is and the second challenge was is uh is and
    the second challenge was is uh is

    writing JVP kernel for arbitrary writing JVP kernel for arbitrary writing JVP
    kernel for arbitrary

    sequence length and because this model sequence length and because this model
    sequence length and because this model

    we we we trained this model with uh uh we we we trained this model with uh uh
    we we we trained this model with uh uh

    with different resolution and different with different resolution and different
    with different resolution and different

    aspect ratio as well. So there were some aspect ratio as well. So there were some
    aspect ratio as well. So there were some

    weird sequence length that came out of weird sequence length that came out of
    weird sequence length that came out of

    it. Um so yeah it it also took a bit of it. Um so yeah it it also took a bit of
    it. Um so yeah it it also took a bit of

    of debugging for writing the JB kernel of debugging for writing the JB kernel
    of debugging for writing the JB kernel

    and yeah uh and we have shown a and yeah uh and we have shown a and yeah uh and
    we have shown a

    step-by-step design to arrive at step-by-step design to arrive at step-by-step
    design to arrive at

    pre-training algorithms that achieve pre-training algorithms that achieve pre-training
    algorithms that achieve

    these three deserter these three deserter these three deserter

    and we can place IM and TVM at the and we can place IM and TVM at the and we can
    place IM and TVM at the

    intersection of of these three intersection of of these three intersection of
    of these three

    categories. Uh yeah and and this is all categories. Uh yeah and and this is all
    categories. Uh yeah and and this is all

    I have for my talk but uh before that uh I have for my talk but uh before that
    uh I have for my talk but uh before that uh

    uh I will take some questions. Uh but uh I will take some questions. Uh but'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 67
  start_sec: 3718.0
  end_sec: 3771.2
  text: 'uh I will take some questions. Uh but

    before that I will I have also have I before that I will I have also have I before
    that I will I have also have I

    was also given a task of of recruiting. was also given a task of of recruiting.
    was also given a task of of recruiting.

    So so yeah I I''ll I''ll just briefly So so yeah I I''ll I''ll just briefly So
    so yeah I I''ll I''ll just briefly

    introduce Luma. Um so Luma is a research introduce Luma. Um so Luma is a research
    introduce Luma. Um so Luma is a research

    and product lab aiming to build and product lab aiming to build and product lab
    aiming to build

    multimodal AGI. Uh and we recently multimodal AGI. Uh and we recently multimodal
    AGI. Uh and we recently

    raised our series C round which uh was raised our series C round which uh was
    raised our series C round which uh was

    uh $900 million and yeah it''s a pretty uh $900 million and yeah it''s a pretty
    uh $900 million and yeah it''s a pretty

    sizable amount. So we have a lot of sizable amount. So we have a lot of sizable
    amount. So we have a lot of

    resource and compute for for us to do resource and compute for for us to do resource
    and compute for for us to do

    research and the and you know the the research and the and you know the the research
    and the and you know the the

    vibe of the company is also very young vibe of the company is also very young
    vibe of the company is also very young

    and the average age it is also very and the average age it is also very and the
    average age it is also very

    young. So, so like you guys um if you young. So, so like you guys um if you young.
    So, so like you guys um if you

    are interested in in us, you can also uh are interested in in us, you can also
    uh are interested in in us, you can also uh

    reach out to me or to to our our team reach out to me or to to our our team'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 68
  start_sec: 3771.2
  end_sec: 3826.079
  text: 'reach out to me or to to our our team

    and uh also the inventors of DDIM and and uh also the inventors of DDIM and and
    uh also the inventors of DDIM and

    Nerf both both work here. So, the mentor Nerf both both work here. So, the mentor
    Nerf both both work here. So, the mentor

    of DDIM, Jaming, is our chief scientist of DDIM, Jaming, is our chief scientist
    of DDIM, Jaming, is our chief scientist

    and and the mentor of Nerf, Matt, uh he and and the mentor of Nerf, Matt, uh he
    and and the mentor of Nerf, Matt, uh he

    he he''s leading our uh applied research he he''s leading our uh applied research
    he he''s leading our uh applied research

    uh team. uh team. uh team.

    And and here here are the roles that And and here here are the roles that And
    and here here are the roles that

    we''re hiring for. So, these are the we''re hiring for. So, these are the we''re
    hiring for. So, these are the

    full-time roles. And if you''re also full-time roles. And if you''re also full-time
    roles. And if you''re also

    interested in internships or or kind of interested in internships or or kind of
    interested in internships or or kind of

    residency type of program uh that that residency type of program uh that that
    residency type of program uh that that

    lasts for 6 months or above, uh please lasts for 6 months or above, uh please
    lasts for 6 months or above, uh please

    also feel feel free to reach out. Uh but also feel feel free to reach out. Uh
    but also feel feel free to reach out. Uh but

    yeah. Okay. I''ll say this much about yeah. Okay. I''ll say this much about yeah.
    Okay. I''ll say this much about

    recruiting but yeah uh I''m I''m I''m happy recruiting but yeah uh I''m I''m I''m
    happy recruiting but yeah uh I''m I''m I''m happy

    to take any question >> all right we have like 10 minutes left >> all right we
    have like 10 minutes left

    feel free to ask questions feel free to ask questions feel free to ask questions

    >> may I ask question so I might be wrong >> may I ask question so I might be
    wrong'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 69
  start_sec: 3826.079
  end_sec: 3867.28
  text: '>> may I ask question so I might be wrong

    but it seems that when you do the but it seems that when you do the but it seems
    that when you do the

    terminal velocity matching at a specific terminal velocity matching at a specific
    terminal velocity matching at a specific

    time t you still need to integrate them time t you still need to integrate them
    time t you still need to integrate them

    over the time t so you do not get rid of over the time t so you do not get rid
    of over the time t so you do not get rid of

    the numerical integ vibration. the numerical integ vibration. the numerical integ
    vibration.

    >> Uh sorry, which uh which slide are you >> Uh sorry, which uh which slide are
    you >> Uh sorry, which uh which slide are you

    talking about? talking about? talking about?

    >> Uh can I go back to the >> Uh can I go back to the >> Uh can I go back to the

    uh maybe next uh maybe next uh maybe next

    >> I feel like yeah if you look at the >> I feel like yeah if you look at the
    >> I feel like yeah if you look at the

    final objective final objective final objective

    >> yeah yeah still still have you still >> yeah yeah still still have you still
    >> yeah yeah still still have you still

    have a integration. Yeah just have a integration. Yeah just have a integration.
    Yeah just

    >> no but the final >> no but the final >> no but the final

    >> uh maybe last last slide >> uh maybe last last slide >> uh maybe last last
    slide

    >> but this that that was their final >> but this that that was their final >>
    but this that that was their final

    objective right? So that was objective right? So that was objective right? So
    that was

    >> this is the final objective. Yes. >> this is the final objective. Yes. >> this
    is the final objective. Yes.

    >> How do you get rid of the integration >> How do you get rid of the integration
    >> How do you get rid of the integration

    time team? Oh uh do you mean the time team? Oh uh do you mean the'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 70
  start_sec: 3867.28
  end_sec: 3917.829
  text: 'time team? Oh uh do you mean the

    integration integration integration

    here? here? here?

    >> Yeah. Over a different time. >> Yeah. Over a different time. >> Yeah. Over
    a different time.

    >> Oh yeah. Yeah. So this is just saying >> Oh yeah. Yeah. So this is just saying
    >> Oh yeah. Yeah. So this is just saying

    that uh so this can be easily done if that uh so this can be easily done if that
    uh so this can be easily done if

    you just do random sample you just do random sample you just do random sample

    like you can randomly sample uh s like you can randomly sample uh s like you can
    randomly sample uh s

    >> for different mini batch you sample >> for different mini batch you sample
    >> for different mini batch you sample

    different times. different times. different times.

    >> Oh. Oh. Oh I see. So so this is not so >> Oh. Oh. Oh I see. So so this is not
    so >> Oh. Oh. Oh I see. So so this is not so

    this is not the final objective that we this is not the final objective that we
    this is not the final objective that we

    want to optimize. So this is just saying want to optimize. So this is just saying
    want to optimize. So this is just saying

    the relationship between the terminal the relationship between the terminal the
    relationship between the terminal

    velocity error and the displacement velocity error and the displacement velocity
    error and the displacement

    error that that you want to ultimately error that that you want to ultimately
    error that that you want to ultimately

    optimize. But the the the the objective optimize. But the the the the objective
    optimize. But the the the the objective

    uh at the end that we optimize for is uh at the end that we optimize for is uh
    at the end that we optimize for is

    this. So the objective is um depends on this. So the objective is um depends on
    this. So the objective is um depends on

    t TN tns only and for the integration um t TN tns only and for the integration
    um t TN tns only and for the integration um

    the the integration only comes in um if'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 71
  start_sec: 3917.829
  end_sec: 3974.4
  text: 'the the integration only comes in um if the the integration only comes in
    um if

    you want to measure its relationship you want to measure its relationship you
    want to measure its relationship

    with respect to the to sign distance. with respect to the to sign distance. with
    respect to the to sign distance.

    >> Yeah. But for the for the final uh >> Yeah. But for the for the final uh >>
    Yeah. But for the for the final uh

    automation goal you you need to specify automation goal you you need to specify
    automation goal you you need to specify

    a time t right? a time t right? a time t right?

    >> Uh yeah yeah yeah. So time t and s are >> Uh yeah yeah yeah. So time t and
    s are >> Uh yeah yeah yeah. So time t and s are

    just random samples uh like you normally just random samples uh like you normally
    just random samples uh like you normally

    do with diffusion models. do with diffusion models. do with diffusion models.

    >> All right. >> All right. >> All right.

    >> Yeah. >> Yeah.

    >> Yeah, that''s a great question. Uh here >> Yeah, that''s a great question.
    Uh here >> Yeah, that''s a great question. Uh here

    this is just for formalizing the this is just for formalizing the this is just
    for formalizing the

    relationship between the displacement relationship between the displacement relationship
    between the displacement

    error and and terminal velocity error. error and and terminal velocity error.
    error and and terminal velocity error.

    So in practice we just randomly sample T So in practice we just randomly sample
    T So in practice we just randomly sample T

    and S. Yeah. and S. Yeah. and S. Yeah.

    >> Any other questions? >> Any other questions? >> Any other questions?

    Okay. Yeah, go ahead. Okay. Yeah, go ahead. Okay. Yeah, go ahead.

    >> Uh, hi Alex. Uh, as you kind of optimize >> Uh, hi Alex. Uh, as you kind of
    optimize >> Uh, hi Alex. Uh, as you kind of optimize

    for the terminal velocity, if is there for the terminal velocity, if is there
    for the terminal velocity, if is there

    any sweet spot for the NFP like with any sweet spot for the NFP like with'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 72
  start_sec: 3974.4
  end_sec: 4023.599
  text: 'any sweet spot for the NFP like with

    four NFP you are getting good quality four NFP you are getting good quality four
    NFP you are getting good quality

    but if you kind of increase it to 50, but if you kind of increase it to 50, but
    if you kind of increase it to 50,

    does the performance actually degrade or does the performance actually degrade
    or does the performance actually degrade or

    still improve? still improve? still improve?

    >> Uh, sorry. So you''re saying during >> Uh, sorry. So you''re saying during
    >> Uh, sorry. So you''re saying during

    inference if you keep increasing the the inference if you keep increasing the
    the inference if you keep increasing the the

    NF, right? NF, right? NF, right?

    >> Yeah. Yeah. >> Yeah. Yeah. >> Yeah. Yeah.

    >> Yeah. So uh you usually it you >> Yeah. So uh you usually it you >> Yeah. So
    uh you usually it you

    experience pretty pretty sharp increase experience pretty pretty sharp increase
    experience pretty pretty sharp increase

    uh for like say four step and then after uh for like say four step and then after
    uh for like say four step and then after

    that the performance can fluctuate. So that the performance can fluctuate. So
    that the performance can fluctuate. So

    it''s not like it''s going to degrade mon it''s not like it''s going to degrade
    mon it''s not like it''s going to degrade mon

    monotonically after some point. So it it monotonically after some point. So it
    it monotonically after some point. So it it

    it generally just fluctuate. So some it generally just fluctuate. So some it generally
    just fluctuate. So some

    some step you''ll get better result and some step you''ll get better result and
    some step you''ll get better result and

    some some not. Yeah. some some not. Yeah. some some not. Yeah.

    >> Okay. uh how how does the sample quality >> Okay. uh how how does the sample
    quality >> Okay. uh how how does the sample quality

    compared to the consistency models like compared to the consistency models like
    compared to the consistency models like

    which do not require training from which do not require training from which do
    not require training from

    scratch like it''s just a distillation scratch like it''s just a distillation'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 73
  start_sec: 4023.599
  end_sec: 4076.4
  text: 'scratch like it''s just a distillation

    approach how is it compared to EVM approach how is it compared to EVM approach
    how is it compared to EVM

    >> uh sorry for do you mean comp compared >> uh sorry for do you mean comp compared
    >> uh sorry for do you mean comp compared

    to uh consensity distillation or to uh consensity distillation or to uh consensity
    distillation or

    consistency training consistency training consistency training

    >> uh the consistency distillation >> uh the consistency distillation >> uh the
    consistency distillation

    >> oh uh so yeah for this work we only we >> oh uh so yeah for this work we only
    we >> oh uh so yeah for this work we only we

    only compared with the training from only compared with the training from only
    compared with the training from

    scratch technique including the scratch technique including the scratch technique
    including the

    diffusion baseline. Uh so we didn''t diffusion baseline. Uh so we didn''t diffusion
    baseline. Uh so we didn''t

    compare with uh with pure dissolation compare with uh with pure dissolation compare
    with uh with pure dissolation

    technique because uh that''s that''s an technique because uh that''s that''s an
    technique because uh that''s that''s an

    entire different species. entire different species. entire different species.

    >> I I think like TVM can be a really good >> I I think like TVM can be a really
    good >> I I think like TVM can be a really good

    teacher in consistency distillation teacher in consistency distillation teacher
    in consistency distillation

    because it has learned the terminal because it has learned the terminal because
    it has learned the terminal

    velocity. velocity. velocity.

    >> Yeah. Yeah. Yeah. Basically if you >> Yeah. Yeah. Yeah. Basically if you >>
    Yeah. Yeah. Yeah. Basically if you

    >> Yeah. Yeah. If you just have this uh the >> Yeah. Yeah. If you just have this
    uh the >> Yeah. Yeah. If you just have this uh the

    first term uh and you use your teacher first term uh and you use your teacher
    first term uh and you use your teacher

    network as the proxy right instead of network as the proxy right instead of network
    as the proxy right instead of

    your own network then then that''s your own network then then that''s'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 74
  start_sec: 4076.4
  end_sec: 4132.719
  text: 'your own network then then that''s

    basically a dissolution technique. Yeah. basically a dissolution technique. Yeah.
    basically a dissolution technique. Yeah.

    >> Thank you. >> Thank you. >> Thank you.

    >> Yeah. >> Yeah.

    >> Any other Yeah. Sure. >> Any other Yeah. Sure. >> Any other Yeah. Sure.

    >> Uh so follow up to that question. You >> Uh so follow up to that question.
    You >> Uh so follow up to that question. You

    mentioned that after a few number of mentioned that after a few number of mentioned
    that after a few number of

    sort of iterations during inference time sort of iterations during inference time
    sort of iterations during inference time

    the performance fluctuates. Can you give the performance fluctuates. Can you give
    the performance fluctuates. Can you give

    more insights as to why that happens and more insights as to why that happens
    and more insights as to why that happens and

    why is it that for like the early on why is it that for like the early on why
    is it that for like the early on

    steps it improves and then >> yeah I um that''s a good question uh I >> yeah I
    um that''s a good question uh I

    think it''s it''s just that the the think it''s it''s just that the the think
    it''s it''s just that the the

    network capacity has has been spent uh network capacity has has been spent uh
    network capacity has has been spent uh

    so you you have very so you you have very so you you have very

    in practice the network capacity is is in practice the network capacity is is
    in practice the network capacity is is

    limited right so it cannot represent uh limited right so it cannot represent uh
    limited right so it cannot represent uh

    so when you optimize for few for few so when you optimize for few for few so when
    you optimize for few for few

    step sampling uh it generally use most step sampling uh it generally use most
    step sampling uh it generally use most

    of the capacity to optimize for for few of the capacity to optimize for for few
    of the capacity to optimize for for few

    step sampling and if you spend more more step sampling and if you spend more more'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 75
  start_sec: 4132.719
  end_sec: 4194.149
  text: 'step sampling and if you spend more more

    more compute on on more intermediate more compute on on more intermediate more
    compute on on more intermediate

    step it doesn''t give you a huge gain um step it doesn''t give you a huge gain
    um step it doesn''t give you a huge gain um

    yeah I I mean I guess I have the question I I mean I guess I have the question

    like it''s the same question. Um, and like it''s the same question. Um, and like
    it''s the same question. Um, and

    like I I feel like people probably also like I I feel like people probably also
    like I I feel like people probably also

    know this because we literally just know this because we literally just know this
    because we literally just

    covered a flow map last class and it''s covered a flow map last class and it''s
    covered a flow map last class and it''s

    probably has like a pretty deep probably has like a pretty deep probably has like
    a pretty deep

    connection to flow maps. Um, yes. connection to flow maps. Um, yes. connection
    to flow maps. Um, yes.

    >> And so yeah, >> And so yeah, >> And so yeah,

    >> if you have seen uh Nick Buffy''s paper, >> if you have seen uh Nick Buffy''s
    paper, >> if you have seen uh Nick Buffy''s paper,

    then yes, we I I also had discussion then yes, we I I also had discussion then
    yes, we I I also had discussion

    with him. uh and yes uh TVM is uh can be with him. uh and yes uh TVM is uh can
    be with him. uh and yes uh TVM is uh can be

    seen as as satisfying the the langian uh seen as as satisfying the the langian
    uh seen as as satisfying the the langian uh

    uh uh constraint if you have learned uh uh constraint if you have learned uh uh
    constraint if you have learned

    about that uh and and yeah so the the about that uh and and yeah so the the about
    that uh and and yeah so the the

    motivation of this paper so what what motivation of this paper so what what motivation
    of this paper so what what

    inspired me uh to write this paper was a'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 76
  start_sec: 4194.149
  end_sec: 4248.4
  text: 'inspired me uh to write this paper was a inspired me uh to write this paper
    was a

    work called um uh physics informed work called um uh physics informed work called
    um uh physics informed

    dissolation for diffusion models uh that dissolation for diffusion models uh that
    dissolation for diffusion models uh that

    came out a few years ago I think uh and came out a few years ago I think uh and
    came out a few years ago I think uh and

    that paper basically uh was using a a a that paper basically uh was using a a
    a that paper basically uh was using a a a

    uh lrangeian formulation for distilling uh lrangeian formulation for distilling
    uh lrangeian formulation for distilling

    for distilling in one step division for distilling in one step division for distilling
    in one step division

    model but it somehow didn''t take off. So model but it somehow didn''t take off.
    So model but it somehow didn''t take off. So

    so I was kind of revisiting uh similar so I was kind of revisiting uh similar
    so I was kind of revisiting uh similar

    concepts and then um uh and then concepts and then um uh and then concepts and
    then um uh and then

    obviously Nick''s paper also also came obviously Nick''s paper also also came
    obviously Nick''s paper also also came

    out uh around the same time. So uh so out uh around the same time. So uh so out
    uh around the same time. So uh so

    yeah so there''s that that definitely a yeah so there''s that that definitely
    a yeah so there''s that that definitely a

    very deep connection uh with the the very deep connection uh with the the very
    deep connection uh with the the

    lrangeian formulation. lrangeian formulation. lrangeian formulation.

    Yeah. Yeah.

    >> Yeah. Great, great, great. Yeah. So, >> Yeah. Great, great, great. Yeah. So,
    >> Yeah. Great, great, great. Yeah. So,

    yeah, for th for those of you who said yeah, for th for those of you who said
    yeah, for th for those of you who said

    like, "Oh, the grunge is so like, "Oh, the grunge is so like, "Oh, the grunge
    is so

    unintuitive." This is why. Okay, now you unintuitive." This is why. Okay, now
    you unintuitive." This is why. Okay, now you

    know. know.'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 77
  start_sec: 4248.4
  end_sec: 4310.07
  text: 'know.

    >> Is there any computational overhead >> Is there any computational overhead
    >> Is there any computational overhead

    since we have a much more complex final since we have a much more complex final
    since we have a much more complex final

    objective objective

    or is it or is it or is it

    >> sorry can I say again? >> sorry can I say again? >> sorry can I say again?

    Is there any computational overhead with Is there any computational overhead with
    Is there any computational overhead with

    the final objective or is it as good as the final objective or is it as good as
    the final objective or is it as good as

    displacement error? displacement error? displacement error?

    >> So yeah, so the the um the the objective >> So yeah, so the the um the the
    objective >> So yeah, so the the um the the objective

    might seem complicated but actually uh might seem complicated but actually uh
    might seem complicated but actually uh

    there it''s not that much complicated there it''s not that much complicated there
    it''s not that much complicated

    because because you can obtain uh in in because because you can obtain uh in in
    because because you can obtain uh in in

    practice you can obtain both f and dfds practice you can obtain both f and dfds
    practice you can obtain both f and dfds

    at the same time. So that''ll give you at the same time. So that''ll give you
    at the same time. So that''ll give you

    this uh the same objective uh and this uh the same objective uh and this uh the
    same objective uh and

    and in practice if you want to save and in practice if you want to save and in
    practice if you want to save

    computational overhead you can also just computational overhead you can also just
    computational overhead you can also just

    randomly sample uh between these two randomly sample uh between these two randomly
    sample uh between these two

    objectives. So so uh so so in essence uh objectives. So so uh so so in essence
    uh objectives. So so uh so so in essence uh

    it it''s in expectation optimizing both it it''s in expectation optimizing both
    it it''s in expectation optimizing both

    objectives at the same at the same time.'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 78
  start_sec: 4310.07
  end_sec: 4359.91
  text: 'objectives at the same at the same time. objectives at the same at the same
    time.

    Um uh so we have observed that if you Um uh so we have observed that if you Um
    uh so we have observed that if you

    optimize both objective at the same time optimize both objective at the same time
    optimize both objective at the same time

    it converges extremely fast. Uh so for it converges extremely fast. Uh so for
    it converges extremely fast. Uh so for

    the entire so training the model to to the entire so training the model to to
    the entire so training the model to to

    convergence the total amount of compute convergence the total amount of compute
    convergence the total amount of compute

    is is not that much higher. >> Okay. Uh I have one last question. So uh >> Okay.
    Uh I have one last question. So uh

    because in my class there are a lot of because in my class there are a lot of
    because in my class there are a lot of

    student who come from like a like come student who come from like a like come
    student who come from like a like come

    from the the robotics institute so they from the the robotics institute so they
    from the the robotics institute so they

    may be more familiar with like shortcut may be more familiar with like shortcut
    may be more familiar with like shortcut

    models and stuff like that and you also models and stuff like that and you also
    models and stuff like that and you also

    you already like um compared with you already like um compared with you already
    like um compared with

    memeflow. So it is there any comparison memeflow. So it is there any comparison
    memeflow. So it is there any comparison

    like have you I I I I think you do you like have you I I I I think you do you
    like have you I I I I think you do you

    have any like comparison uh with like have any like comparison uh with like have
    any like comparison uh with like

    shortcut model or like basically in shortcut model or like basically in shortcut
    model or like basically in

    terms of performance or in terms of like'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 79
  start_sec: 4359.91
  end_sec: 4414.08
  text: 'terms of performance or in terms of like terms of performance or in terms
    of like

    training stabilities like like yeah training stabilities like like yeah training
    stabilities like like yeah

    basically what is what was your basically what is what was your basically what
    is what was your

    observation there? observation there? observation there?

    >> Yeah. So sh model. So I I compared with >> Yeah. So sh model. So I I compared
    with >> Yeah. So sh model. So I I compared with

    Shan model uh in my previous paper the Shan model uh in my previous paper the
    Shan model uh in my previous paper the

    IMN paper we compared to shortcom model. IMN paper we compared to shortcom model.
    IMN paper we compared to shortcom model.

    Uh but but I think uh Uh but but I think uh Uh but but I think uh

    there was no um like followup to to that there was no um like followup to to that
    there was no um like followup to to that

    line of work. So so the performance um line of work. So so the performance um
    line of work. So so the performance um

    uh the performance reported was not uh the performance reported was not uh the
    performance reported was not

    super competitive. Uh so in this paper super competitive. Uh so in this paper
    super competitive. Uh so in this paper

    we we just left left that out. uh and we we just left left that out. uh and we
    we just left left that out. uh and

    and compared to more more uh more recent and compared to more more uh more recent
    and compared to more more uh more recent

    and more relevant more performance and more relevant more performance and more
    relevant more performance

    baselines. Uh but yes uh in general I baselines. Uh but yes uh in general I baselines.
    Uh but yes uh in general I

    think sh model it doesn''t since it think sh model it doesn''t since it think
    sh model it doesn''t since it

    doesn''t require the the the different doesn''t require the the the different
    doesn''t require the the the different

    the differentiation. Uh so I think shel the differentiation. Uh so I think shel
    the differentiation. Uh so I think shel

    models in general still has some models in general still has some'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
- idx: 80
  start_sec: 4414.08
  end_sec: 4472.239
  text: 'models in general still has some

    advantage in terms of training training advantage in terms of training training
    advantage in terms of training training

    uh uh training simplicity I guess. Um uh uh training simplicity I guess. Um uh
    uh training simplicity I guess. Um

    uh but in terms of performance, I have uh but in terms of performance, I have
    uh but in terms of performance, I have

    not seen uh uh I I I have not seen an not seen uh uh I I I have not seen an not
    seen uh uh I I I have not seen an

    updated version uh of that line of work updated version uh of that line of work
    updated version uh of that line of work

    that that is competitive yet uh to to that that is competitive yet uh to to that
    that is competitive yet uh to to

    both the the flow or or uh something both the the flow or or uh something both
    the the flow or or uh something

    like TBM. So like TBM. So like TBM. So

    >> hey, great. All right. Seems like we''re >> hey, great. All right. Seems like
    we''re >> hey, great. All right. Seems like we''re

    running out of time. Any running out of time. Any running out of time. Any

    like Okay. Okay. One last question. like Okay. Okay. One last question. like Okay.
    Okay. One last question.

    Okay. Okay. Okay.

    >> Okay. >> Okay. >> Okay.

    >> Have you tried TVM with like DPM solver >> Have you tried TVM with like DPM
    solver >> Have you tried TVM with like DPM solver

    or other solvers? How does it compare or other solvers? How does it compare or
    other solvers? How does it compare

    then? Because we are doing it with DDIM. then? Because we are doing it with DDIM.
    then? Because we are doing it with DDIM.

    >> Oh. Uh as in how do you parameterize F, >> Oh. Uh as in how do you parameterize
    F, >> Oh. Uh as in how do you parameterize F,

    right? right? right?

    >> Yeah. Uh I think >> Yeah. Uh I think >> Yeah. Uh I think

    >> no. Uh but that''s a great uh I think to >> no. Uh but that''s a great uh I
    think to'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 81
  start_sec: 4472.239
  end_sec: 4528.0
  text: '>> no. Uh but that''s a great uh I think to

    to study uh because for we only used the to study uh because for we only used
    the to study uh because for we only used the

    DDIM uh uh the the the DDM form of F for DDIM uh uh the the the DDM form of F
    for DDIM uh uh the the the DDM form of F for

    simplicity and we didn''t actually try to simplicity and we didn''t actually try
    to simplicity and we didn''t actually try to

    investigate some other forms uh which investigate some other forms uh which investigate
    some other forms uh which

    might work better. But I think that''s a might work better. But I think that''s
    a might work better. But I think that''s a

    valid question and I my intuition is valid question and I my intuition is valid
    question and I my intuition is

    that there there can exist better uh f that there there can exist better uh f
    that there there can exist better uh f

    form. So yeah. form. So yeah. form. So yeah.

    >> Okay. Cool. All right. Uh I guess that''s >> Okay. Cool. All right. Uh I guess
    that''s >> Okay. Cool. All right. Uh I guess that''s

    it for today''s lecture. Yeah. Thank you it for today''s lecture. Yeah. Thank
    you it for today''s lecture. Yeah. Thank you

    so much Alex for giving this amazing so much Alex for giving this amazing so much
    Alex for giving this amazing

    talk and I hope everyone learned a lot talk and I hope everyone learned a lot
    talk and I hope everyone learned a lot

    about you know the state-of-the-art of about you know the state-of-the-art of
    about you know the state-of-the-art of

    the you know few step and onestep the you know few step and onestep the you know
    few step and onestep

    models. Uh but yeah and yeah, Alex and models. Uh but yeah and yeah, Alex and
    models. Uh but yeah and yeah, Alex and

    Mua is recruiting so you know. Mua is recruiting so you know. Mua is recruiting
    so you know.

    >> Oh yes uh we''re recruit so please reach >> Oh yes uh we''re recruit so please
    reach >> Oh yes uh we''re recruit so please reach

    out. out.'
  concept_slugs:
  - ddim
  - latent-diffusion
  - video-diffusion
- idx: 82
  start_sec: 4528.0
  end_sec: 4549.239
  text: 'out.

    >> Yeah, please reach out. Um yeah and Alex >> Yeah, please reach out. Um yeah
    and Alex >> Yeah, please reach out. Um yeah and Alex

    can if you can share with me with the can if you can share with me with the can
    if you can share with me with the

    the slide and I can link the slides to the slide and I can link the slides to
    the slide and I can link the slides to

    the website and then people can click on the website and then people can click
    on the website and then people can click on

    the links if the Yeah, basically. the links if the Yeah, basically. the links
    if the Yeah, basically.

    >> Yeah. Yeah. Yeah. Sure. Sure. Yeah. And >> Yeah. Yeah. Yeah. Sure. Sure. Yeah.
    And >> Yeah. Yeah. Yeah. Sure. Sure. Yeah. And

    thanks so much for the invite. thanks so much for the invite. thanks so much for
    the invite.

    >> Yeah, no problem. Okay. Yeah, the class >> Yeah, no problem. Okay. Yeah, the
    class >> Yeah, no problem. Okay. Yeah, the class

    is over. Yeah. Thank you so much, Alex. is over. Yeah. Thank you so much, Alex.
    is over. Yeah. Thank you so much, Alex.

    Yeah. Thank you.'
  concept_slugs:
  - latent-diffusion
  - video-diffusion
---
# CMU 10799 S26: Lecture 11 - Guest Lecture Linqi (Alex) Zhou from Luma AI - Diffusion & Flow Matching

See the structured chunks above.
