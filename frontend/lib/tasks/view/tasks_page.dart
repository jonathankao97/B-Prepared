import 'package:flutter/material.dart';

class TasksPage extends StatelessWidget {
  const TasksPage({Key? key}) : super(key: key);

  static Page page() => const MaterialPage<void>(child: TasksPage());

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Tasks Page'),
    );
  }
}
